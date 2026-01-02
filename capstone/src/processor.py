import multiprocessing
import os
import logging
import json
import uuid
import random
from src.schema import SchemaParser
from src.data_generator import DataGenerator

class DataProcessor:
    """Responsible for spawning multiple processes, managing workers and jobs."""

    def __init__(self, args):
        self.args = args
        self.generator = DataGenerator()
        self.parser = SchemaParser(args.data_schema, self.generator)

    def _run_job(self, worker_id, num_files):
        for i in range(num_files):
            prefix = self._get_prefix(worker_id, i)
            filename = f"{prefix}_{self.args.file_name}.json"
            filepath = os.path.join(self.args.path_to_save_files, filename)

            # try:
            with open(filepath, 'w', encoding='utf-8') as f:
                for _ in range(self.args.data_lines):
                    line_dict = self.parser.generate_line()
                    f.write(json.dumps(line_dict) + '\n')
            # except Exception as e:
            #     logging.error("Worker %s failed to write %s: %s", worker_id, filename, e)
            #     sys.exit(1)

    def _get_prefix(self, worker_id, file_idx):
        if self.args.file_prefix == 'count':
            return f"{worker_id}_{file_idx}"
        if self.args.file_prefix == 'uuid':
            return str(uuid.uuid4())
        return str(random.randint(1000, 9999))

    def execute(self):
        if self.args.files_count == 0:
            for _ in range(self.args.data_lines):
                print(json.dumps(self.parser.generate_line()))
            return

        num_procs = max(1, min(self.args.multiprocessing, os.cpu_count() or 1))
        files_per_proc = self.args.files_count // num_procs
        remainder = self.args.files_count % num_procs

        logging.info("Creating %s processes for %s files.", num_procs, self.args.files_count)

        processes = []
        for i in range(num_procs):
            count = files_per_proc + (1 if i < remainder else 0)
            if count == 0:
                continue

            p = multiprocessing.Process(target=self._run_job, args=(i, count))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
