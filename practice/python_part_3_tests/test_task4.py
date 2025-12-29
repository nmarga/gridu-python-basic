"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
import sys
from faker import Faker
import pytest
from python_part_3.task4 import print_name_address, parse_args_helper

def test_print_name_address(monkeypatch, capfd):
    """Test print_name_address function"""

    # Seed for same faker results
    Faker.seed(42)

    monkeypatch.setattr(sys, "argv",
                        ["task3.py", "3", "--fake-number=phone_number", "--some_string=word"])

    cmd_args = parse_args_helper()
    print_name_address(cmd_args)
    captured = capfd.readouterr()
    expected_result = "{'fake_number': '+1-210-343-3218x1960', 'some_string': 'discover'}\n"
    expected_result += "{'fake_number': '989.608.3863', 'some_string': 'table'}\n"
    expected_result += "{'fake_number': '3268542351', 'some_string': 'bill'}\n"

    assert captured.out == expected_result

    # Test case with number 0
    monkeypatch.setattr(sys, "argv",
                        ["task3.py", "0"])

    cmd_args = parse_args_helper()
    print_name_address(cmd_args)
    captured = capfd.readouterr()
    expected_result = ""

    assert captured.out == expected_result


def test_print_name_address_exception(monkeypatch):
    """Test print_name_address function exceptions"""

    monkeypatch.setattr(sys, "argv",
                        ["task3.py", "not_integer"])

    cmd_args = parse_args_helper()
    with pytest.raises(ValueError):
        print_name_address(cmd_args)

def test_print_name_address_unkown_field_exception(monkeypatch):
    """Test print_name_address function exception for unkown field"""

    monkeypatch.setattr(sys, "argv",
                        ["task3.py", "3", "--fake-number=unkown_field_type", "--some_string=word"])

    cmd_args = parse_args_helper()
    with pytest.raises(AttributeError):
        print_name_address(cmd_args)
