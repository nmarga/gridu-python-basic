import json
import os
import logging
import sys
from typing import Any, Dict, Union

class SchemaParser:
    """Parses the schema definitions in the args and generates data objects."""

    engine: Any
    raw_schema: Dict[str, str]

    def __init__(self, schema_input: str, generator_engine: Any) -> None:
        self.engine = generator_engine
        self.raw_schema = self._load_json(schema_input)

    def _load_json(self, source: str) -> Dict[str, str]:
        """Loads JSON from a file path or a raw string."""
        try:
            if os.path.isfile(source):
                with open(source, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return json.loads(source)
        except json.JSONDecodeError as e:
            logging.error("Schema Error: Could not parse JSON. %s", e)
            sys.exit(1)

    def generate_line(self) -> Dict[str, Union[str, int]]:
        """Generates a single dictionary based on schema rules."""
        line: Dict[str, Union[str, int]] = {}

        for key, value in self.raw_schema.items():
            if ':' not in value:
                logging.error("Invalid schema format for '%s': %s", key, value)
                sys.exit(1)

            parts = [x.strip() for x in value.split(':', 1)]
            dtype: str = parts[0]
            instruction: str = parts[1] if len(parts) > 1 else ""

            if dtype == 'timestamp':
                if instruction:
                    logging.warning("timestamp does not support values: %s", instruction)
                line[key] = self.engine.get_timestamp(instruction)
            elif dtype == 'str':
                line[key] = self.engine.get_str(instruction)
            elif dtype == 'int':
                line[key] = self.engine.get_int(instruction)
            else:
                logging.error("Unsupported type '%s' for key '%s'", dtype, key)
                sys.exit(1)
        return line
