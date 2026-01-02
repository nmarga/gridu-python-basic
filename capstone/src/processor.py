import multiprocessing
import os
import logging
import json
import uuid
import random
import argparse
import sys
from typing import List
from src.schema import SchemaParser
from src.data_generator import DataGenerator

class DataProcessor:
    """Responsible for spawning multiple processes, managing workers and jobs."""

    args: argparse.Namespace
    generator: DataGenerator
    parser: SchemaParser

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.generator = DataGenerator()
        self.parser = SchemaParser(args.data_schema, self.generator)

    def _run_job(self, worker_id: int, num_files: int) -> None:
        """Process target: generates a set number of files."""
        for i in range(num_files):
            prefix = self._get_prefix(worker_id, i)
            filename = f"{self.args.file_name}_{prefix}.json"
            filepath = os.path.join(self.args.path_to_save_files, filename)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    for _ in range(self.args.data_lines):
                        line_dict: dict = self.parser.generate_line()
                        f.write(json.dumps(line_dict) + '\n')
            except OSError as e:
                logging.error("Worker %s failed to write %s: %s", worker_id, filename, e)
                return

    def _get_prefix(self, worker_id: int, file_idx: int) -> str:
        """Generates a filename prefix based on the chosen strategy."""
        if self.args.file_prefix == 'count':
            return f"{worker_id}_{file_idx}"
        if self.args.file_prefix == 'uuid':
            return str(uuid.uuid4())
        return str(random.randint(1000, 9999))

    def execute(self) -> None:
        """Starts the data generation process."""
        if self.args.files_count < 0:
            logging.error("Configuration Error: files_count cannot be less than 0. Got: %s",
                        self.args.files_count)
            sys.exit(1)

        if self.args.files_count == 0:
            for _ in range(self.args.data_lines):
                print(json.dumps(self.parser.generate_line()))
            return

        # Check if directory exists
        if not os.path.exists(self.args.path_to_save_files):
            os.makedirs(self.args.path_to_save_files, exist_ok=True)

        cpu_count = os.cpu_count() or 1
        num_procs = max(1, min(self.args.multiprocessing, cpu_count))

        files_per_proc = self.args.files_count // num_procs
        remainder = self.args.files_count % num_procs

        logging.info("Creating %s processes for %s files.", num_procs, self.args.files_count)

        processes: List[multiprocessing.Process] = []
        for i in range(num_procs):
            count = files_per_proc + (1 if i < remainder else 0)
            if count == 0:
                continue

            p = multiprocessing.Process(target=self._run_job, args=(i, count))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
