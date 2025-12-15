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
    Deletes an element from any type of list.

    Args:
        list_to_clean (List): List of elements.
        item_to_delete (Any): The item to be removed from the list.

    Returns:
        List: A list with the removed item.
    """

    # Extract all indexes from the list where the value is equal to item_to_delete
    indexes_to_delete = [index for index, _ in enumerate(list_to_clean)
                         if list_to_clean[index] == item_to_delete]

    # The list must be sorted in reverse order
    # pop() method changes the indexeses after the n-th popped element.
    for index in sorted(indexes_to_delete, reverse=True):
        list_to_clean.pop(index)

    return list_to_clean
