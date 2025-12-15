"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    """
    Updates a dictionary with defined values if the new value is more than in the dictionary.

    Args:
        dict_to_update (Dict[str, str]): Dictionary to update.
        **items_to_set: Items to set.

    Returns:
        Dict: Updated dictionary.
    """
    # Iterating through each key value in the items_to_set
    for item in items_to_set:

        # Extracting the values from the items
        dict_value = dict_to_update.get(item)
        new_value = items_to_set.get(item)

        # Check if the dict_value actually exist in the dictonary, if not, add it
        if dict_value is None:
            dict_to_update[item] = new_value
            # Skip this iteration
            continue

        # Compare original dictionary value with the new value from the items_to_set parameter
        if dict_value < new_value:
            dict_to_update[item] = new_value

    return dict_to_update
