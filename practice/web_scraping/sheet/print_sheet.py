"""PrintSheet implementation."""
from typing import Dict, List
import prettytable

class PrintSheet:
    """Implementation for printing tables from a dictionary."""

    @staticmethod
    def print_table(sheet: Dict, field_names: List, column_codes: List, table_title: str) -> None:
        """Prints the configured table format."""
        table = prettytable.PrettyTable()

        table.field_names = field_names
        table.junction_char = "-"
        table.horizontal_char = "-"
        table.vertical_char = "|"
        table.align = "l"
        table.hrules = prettytable.HEADER

        # Add Data
        for key, _ in sheet.items():
            table.add_row([sheet[key]['name'], key]
                          + [sheet[key][column_code] for column_code in column_codes])

        table_str = table.get_string()

        # Create Custom Banner
        header_title = table_title
        table_width = len(table_str.split('\n', maxsplit=1)[0])
        banner = f"{header_title:=^{table_width}}"
        bottom_line = "-"*table_width

        # Print Final Result
        print(banner)
        print(table_str)
        print(bottom_line)
