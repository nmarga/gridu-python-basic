"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    """
    Enumerates unique words and rebuilds a string from all words of a given number
    
    :param lines: Lines with words
    :type lines: Iterable[str]
    :param word_number: The index of the word to extract from the lines
    :type word_number: int
    :return:
    :rtype: str
    """

    if word_number < 0:
        raise ValueError("word_number cannot be smaller than 0")
    
    # Create a list to store all the words from each line
    word_list_lines = []

    # Iterate through the lines
    for line in lines:

        # Create a dictionary to store the word and its index
        unique_word_dict = {}

        # Set the word index
        word_index = 0
        word_list = line.split(' ')

        # Clear the empty words
        while '' in word_list:
            word_list.remove('')

        for word in word_list:

            # Check if the word already exist in the dictionary
            if unique_word_dict.get(word.strip()) != None:
                # Skip the word if found
                continue

            # Strip the word of other white spaces left
            unique_word_dict[word.strip()] = word_index
            word_index += 1
        
        word_list_lines += [word for word in unique_word_dict if unique_word_dict.get(word) == word_number]

    # Merge the word list into a final string
    return ' '.join(word_list_lines)

