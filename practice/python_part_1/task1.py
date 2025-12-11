"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any


def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    """
    Deletes an element from any type of list
    
    :param list_to_clean: The list to clean
    :type list_to_clean: List
    :param item_to_delete: The item to delete from the list
    :type item_to_delete: Any
    :return:
    :rtype: List
    """
    # Extract all elements from the list that are not equal to item_to_delete
    # It uses List Comprehensions
    return [item for item in list_to_clean if item != item_to_delete]