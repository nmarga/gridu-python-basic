"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""
import argparse
import faker

def print_name_address(args: argparse.Namespace) -> None:
    """Generates defined number of dicts separated by new line based on the command arguments."""

    factory_faker = faker.Factory.create()

    args_dict = vars(args)
    output_list = []
    output_num = int(args_dict.pop("NUMBER"))

    for _ in range(output_num):
        output_list.append({key: factory_faker.format(value) for key, value in args_dict.items()})

    for output_row in output_list:
        print(output_row)


def parse_args_helper() -> argparse.Namespace:
    """Helper function to process command line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("NUMBER")
    _, unkown_args = parser.parse_known_args()

    for unkown_arg in unkown_args:
        parser.add_argument(
            unkown_arg.split('=')[0]
        )

    return parser.parse_args()

if __name__ == "__main__":

    cmd_args = parse_args_helper()
    print_name_address(cmd_args)
