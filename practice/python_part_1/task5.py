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

    # Create a dictionary to store the word
    unique_word_dict = {}

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
        unique_word_dict[word.strip()] = True
    
    # Merge the words into a list then join this list sepparated by a space
    return ' '.join([word for word in unique_word_dict])