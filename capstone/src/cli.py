import argparse
import configparser
import os
import sys
import logging
from typing import Dict, Any, Callable, Optional

class CLIHandler:
    config_path: str
    defaults: Dict
    parser: argparse.ArgumentParser

    def __init__(self, config_path: Optional[str] = None) -> None:
        if config_path:
            self.config_path = config_path
        else:
            current_dir: str = os.path.dirname(os.path.abspath(__file__))
            self.config_path = os.path.join(current_dir, '..', 'config/default.ini')

        self.defaults = self._load_defaults()
        self.parser = argparse.ArgumentParser(
            prog="MagicGenerator",
            description="Console utility for generating JSON test data based on a schema."
        )

    def _load_defaults(self) -> Dict[str, str]:
        """Load configuration from default.ini file."""
        config: configparser.ConfigParser = configparser.ConfigParser()

        if not os.path.exists(self.config_path):
            logging.error("Critical Error: Configuration file not found at %s", self.config_path)
            sys.exit(1)

        config.read(self.config_path)

        if 'AppConfig' not in config.sections():
            logging.error("Critical Error: [AppConfig] section missing in %s", self.config_path)
            sys.exit(1)

        return dict(config.items('AppConfig'))

    def _get_val(self, key: str, type_func: Callable[[str], Any]) -> Any:
        """Read a value from the defaults dictionary and then type cast it."""
        if key not in self.defaults:
            logging.error("Configuration Error: Key '%s' is missing from %s", key, self.config_path)
            sys.exit(1)

        raw_val: str = self.defaults[key]
        try:
            return type_func(raw_val)
        except (ValueError, TypeError):
            logging.error(
                "Type Error: Key '%s' with value '%s' cannot be converted to %s", 
                key, raw_val, type_func.__name__
            )
            sys.exit(1)

    def parse(self) -> argparse.Namespace:
        """Defines arguments using the .ini file."""
        self.parser.add_argument(
            "path_to_save_files",
            nargs='?',
            default=self._get_val('path_to_save_files', str),
            help="Path where all generated files will be saved"
        )

        self.parser.add_argument(
            "--files_count", 
            type=int,
            default=self._get_val('files_count', int),
            help="Number of JSON files to generate"
        )

        self.parser.add_argument(
            "--file_name",
            default=self._get_val('file_name', str),
            help="Base name for the generated files"
        )

        self.parser.add_argument(
            "--file_prefix", 
            choices=['count', 'random', 'uuid'],
            default=self._get_val('file_prefix', str),
            help="Prefix type for filenames if files_count > 1"
        )

        self.parser.add_argument(
            "--data_schema",
            default=self._get_val('data_schema', str),
            help="JSON string or path to a JSON file containing the data schema"
        )

        self.parser.add_argument(
            "--data_lines", 
            type=int,
            default=self._get_val('data_lines', int),
            help="Number of data lines per file"
        )

        clear_str: str = self.defaults.get('clear_path', 'False')
        clear_def: bool = clear_str.lower() == 'true'

        self.parser.add_argument(
            "--clear_path", 
            action='store_true',
            default=clear_def,
            help="If set, deletes files in the target path that match file_name before starting"
        )

        self.parser.add_argument(
            "--multiprocessing", 
            type=int,
            default=self._get_val('multiprocessing', int),
            help="Number of parallel processes to use"
        )

        return self.parser.parse_args()
