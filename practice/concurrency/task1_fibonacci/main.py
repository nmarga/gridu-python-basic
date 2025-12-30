import os
import csv
import sys
from random import randint
from typing import Tuple, List
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'
sys.set_int_max_str_digits(0)


def fib(n: int) -> int:
    """Calculate a value in the Fibonacci sequence by ordinal number"""
    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1

def save_fib_to_file(n: int) -> None:
    """Helper to calculate and save a single file (used by func1)"""
    value = fib(n)
    file_path = os.path.join(OUTPUT_DIR, f"{n}.txt")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(value))

def read_fib_file(filename: str) -> Tuple:
    """Helper to read a file and return (ordinal, value) (used by func2)"""
    ordinal = filename.replace('.txt', '')
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        value = f.read().strip()
    return ordinal, value

def func1(array: List) -> None:
    """Calculate the Fibonacci values and writes them to separate files."""
    # Use ProcessPoolExecutor for CPU-bound tasks
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(save_fib_to_file, array)

def func2(result_file: str) -> None:
    """Create a CSV file after reading files from OUTPUT_DIR."""
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.txt')]

    # Use ThreadPoolExecutor for I/O-bound tasks
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(read_fib_file, files))

    # Write results to the CSV
    with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(results)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
