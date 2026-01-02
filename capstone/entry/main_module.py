import logging
import os
import sys
from src.cli import CLIHandler
from src.processor import DataProcessor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main() -> None:
    # Parse args
    cli = CLIHandler()
    args = cli.parse()

    # Path validation
    if not os.path.exists(args.path_to_save_files):
        os.makedirs(args.path_to_save_files)
    elif not os.path.isdir(args.path_to_save_files):
        sys.exit(1)

    if args.clear_path:
        logging.info("Cleaning target directory...")
        for f in os.listdir(args.path_to_save_files):
            os.remove(os.path.join(args.path_to_save_files, f))

    # Execute workers
    processor = DataProcessor(args)
    logging.info("Generation started.")
    processor.execute()
    logging.info("Generation finished successfully.")

if __name__ == "__main__":
    main()
