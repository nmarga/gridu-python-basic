# Magic Generator Capstone Task

A console utility for generating data using multiprocessing.

## Installation

To install the package go into ./capstone directory and run:
```bash
pip install .
```

## Usage
Once installed, the magicgenerator command will be available in the terminal.

```bash
magicgenerator [path_to_save] [options]
```
You can check the list of arguments via the following command:
```bash
magicgenerator --help
```

## Example
The following command generates 100 JSON files using 10 parallel processes, applies the data schema, and clears the target directory before starting:
```bash
magicgenerator ./output \
  --files_count=100 \
  --file_name=test_data \
  --file_prefix=uuid \
  --multiprocessing=10 \
  --data_schema="{\"date\":\"timestamp:\", \"name\":\"str:rand\", \"type\":\"str:['client', 'partner']\", \"age\":\"int:rand(1, 90)\"}" \
  --clear_path
```