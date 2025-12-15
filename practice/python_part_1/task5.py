"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    """
    Removes duplicate words from a line of space sepparated words
    
    :param line: The line string
    :type line: str
    :return:
    :rtype: str
    """

    # Split the line, convert to a dictionary then extract the keys from it into a list
    word_list = list(dict.fromkeys(line.split()))
    
    # Join this list sepparated by a space
    return ' '.join(word_list)