import uuid
import random
import time
import re

class DataGenerator:
    """DataGenerator class for converting the transformation of schema instructions into data."""
    @staticmethod
    def get_timestamp(_):
        return str(time.time())

    @staticmethod
    def get_str(instruction):
        if instruction == 'rand':
            return str(uuid.uuid4())
        if instruction.startswith('[') and instruction.endswith(']'):
            items = [i.strip().strip("'").strip('"') for i in instruction[1:-1].split(',')]
            return str(random.choice(items))
        return instruction

    @staticmethod
    def get_int(instruction):
        if instruction == 'rand':
            return random.randint(0, 10000)

        # Match rand(from, to)
        range_match = re.match(r'rand\((\d+),\s*(\d+)\)', instruction)
        if range_match:
            start, end = map(int, range_match.groups())
            return random.randint(start, end)

        if instruction.startswith('[') and instruction.endswith(']'):
            items = [i.strip() for i in instruction[1:-1].split(',')]
            return int(random.choice(items))

        return int(instruction)
