import os
import pytest
from html_parser.parser import Parser

TEST_CASES = [
    ("12K", 12000),
    ("31.43M", 31430000),
    ("2.913B", 2913000000),
    ("0.54M", 540000),
    ("54.3K", 54300),
]

@pytest.mark.parametrize(["str_num", "val_num"], TEST_CASES)
def test_convert_to_int_parser(str_num: str, val_num: int):
    """Test the convert to int helper methodd from the parser."""
    assert Parser.convert_to_int(str_num) == val_num

def test_active_stocks_parser():
    """Test the active stocks parser."""
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, './mock_response.html'), 'r', encoding='utf-8') as f:
        assert Parser.parse_stocks(f.read()) == {
            'NVDA': 'NVIDIA Corporation', 'TSLA': 'Tesla, Inc.',
            'PLUG': 'Plug Power Inc.', 'ONDS': 'Ondas Holdings Inc.',
            'NIO': 'NIO Inc.', 'OPEN': 'Opendoor Technologies Inc.',
            'BBAI': 'BigBear.ai Holdings, Inc.', 'AAL': 'American Airlines Group Inc.',
            'QBTS': 'D-Wave Quantum Inc.', 'BMNR': 'Bitmine Immersion Technologies, Inc.',
            'ABEV': 'Ambev S.A.', 'CPNG': 'Coupang, Inc.', 'INTC': 'Intel Corporation', 
            'MARA': 'MARA Holdings, Inc.', 'RGTI': 'Rigetti Computing, Inc.',
            'WBD': 'Warner Bros. Discovery, Inc.', 'PLTR': 'Palantir Technologies Inc.',
            'SMR': 'NuScale Power Corporation', 'SOFI': 'SoFi Technologies, Inc.',
            'PSLV': 'Sprott Physical Silver Trust', 'RKLB': 'Rocket Lab Corporation',
            'F': 'Ford Motor Company', 'NKE': 'NIKE, Inc.', 
            'NFLX': 'Netflix, Inc.', 'AG': 'First Majestic Silver Corp.'
        }
