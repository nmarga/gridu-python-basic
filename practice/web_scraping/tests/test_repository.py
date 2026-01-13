import pytest
from repository.data_repository import DataRepository

@pytest.fixture(name="data_repository")
def fixture_data_repository():
    """Fixture for DataRepository object."""
    data_rep = DataRepository()
    yield data_rep

    # Clear the repository
    data_rep.profile_data = {}
    data_rep.holders_data = {}
    data_rep.stats_data = {}
    data_rep.stock_data = {}

def test_insertion_data_repository(data_repository):
    """Test new data insertions into the repository."""
    data_repository.insert_stock_data({'NVDA': 'NVIDIA Corporation',
                                       'TSLA': 'Tesla, Inc.'})
    assert data_repository.stock_data == {
        'NVDA': 'NVIDIA Corporation',
        'TSLA': 'Tesla, Inc.'
    }

    data_repository.insert_profile_data(
        {'NVDA': {'country': 'United States',
                'employees': 36000, 'ceo_name': 'Mr. Jen-Hsun  Huang',
                'ceo_year_born': 1963},
        'TSLA': {'country': 'United States',
                'employees': 125665, 'ceo_name': 'Mr. Elon R. Musk',
                'ceo_year_born': 1971}})

    assert data_repository.profile_data == {
        'NVDA': {'country': 'United States',
                'employees': 36000, 'ceo_name': 'Mr. Jen-Hsun  Huang',
                'ceo_year_born': 1963},
        'TSLA': {'country': 'United States',
                'employees': 125665, 'ceo_name': 'Mr. Elon R. Musk',
                'ceo_year_born': 1971}
    }

    data_repository.insert_stats_data({
        'NVDA': {'week_change_52': 38.58, 'total_cash': '4.63T'}, 
        'TSLA': {'week_change_52': 13.84, 'total_cash': '1.58T'}})

    assert data_repository.stats_data == {
        'NVDA': {'week_change_52': 38.58, 'total_cash': '4.63T'}, 
        'TSLA': {'week_change_52': 13.84, 'total_cash': '1.58T'}
    }

    data_repository.insert_holders_data({
        'NVDA': 
        {'shares': 1930000000, 'date_reported': 'Sep 30, 2025',
         'per_out': '7.94%', 'value': '367,581,742,351'},
        'TSLA': 
        {'shares': 206740000, 'date_reported': 'Sep 30, 2025',
         'per_out': '6.22%', 'value': '98,240,638,072'}})

    assert data_repository.holders_data == {
        'NVDA': 
        {'shares': 1930000000, 'date_reported': 'Sep 30, 2025',
         'per_out': '7.94%', 'value': '367,581,742,351'},
        'TSLA': 
        {'shares': 206740000, 'date_reported': 'Sep 30, 2025',
         'per_out': '6.22%', 'value': '98,240,638,072'}
    }

def test_joins_data_repository(data_repository):
    """Test the joins."""
    assert data_repository.get_youngest_ceos(1) == {
        'TSLA': {'country': 'United States',
        'employees': 125665, 'ceo_name': 'Mr. Elon R. Musk',
        'ceo_year_born': 1971, 'name': 'Tesla, Inc.'}
    }
    assert data_repository.get_largest_holds(1) == {
        'NVDA': 
        {'shares': 1930000000, 'date_reported': 'Sep 30, 2025',
         'per_out': '7.94%', 'value': '367,581,742,351', 'name': 'NVIDIA Corporation'}
    }
    assert data_repository.get_best_change(1) == {
        'NVDA': {'week_change_52': 38.58, 'total_cash': '4.63T', 'name': 'NVIDIA Corporation'}
    }

def test_repository_data(data_repository):
    """Tests the repository state after the joins."""
    assert data_repository.stock_data == {
        'NVDA': 'NVIDIA Corporation',
        'TSLA': 'Tesla, Inc.'
    }
    assert data_repository.profile_data == {
        'NVDA': {'country': 'United States',
                'employees': 36000, 'ceo_name': 'Mr. Jen-Hsun  Huang',
                'ceo_year_born': 1963},
        'TSLA': {'country': 'United States',
                'employees': 125665, 'ceo_name': 'Mr. Elon R. Musk',
                'ceo_year_born': 1971}
    }
    assert data_repository.stats_data == {
        'NVDA': {'week_change_52': 38.58, 'total_cash': '4.63T'}, 
        'TSLA': {'week_change_52': 13.84, 'total_cash': '1.58T'}
    }
    assert data_repository.holders_data == {
        'NVDA': 
        {'shares': 1930000000, 'date_reported': 'Sep 30, 2025',
         'per_out': '7.94%', 'value': '367,581,742,351'},
        'TSLA': 
        {'shares': 206740000, 'date_reported': 'Sep 30, 2025',
         'per_out': '6.22%', 'value': '98,240,638,072'}
    }
