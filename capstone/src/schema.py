import json
import os
import logging
import sys

class SchemaParser:
    """Parses the schema defenitions in the args."""
    def __init__(self, schema_input, generator_engine):
        self.engine = generator_engine
        self.raw_schema = self._load_json(schema_input)

    def _load_json(self, source):
        try:
            if os.path.isfile(source):
                with open(source, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return json.loads(source)
        except json.JSONDecodeError as e:
            logging.error("Schema Error: Could not parse JSON. %s", e)
            sys.exit(1)

    def generate_line(self):
        """Generates a single dictionary based on schema rules."""
        line = {}
        for key, value in self.raw_schema.items():
            if ':' not in value:
                logging.error("Invalid schema format for '%s': %s", key, value)
                sys.exit(1)

            dtype, instruction = [x.strip() for x in value.split(':', 1)]

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
