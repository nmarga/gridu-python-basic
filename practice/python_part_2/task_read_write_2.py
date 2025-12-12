"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def write_random_words(word_count=10) -> None:
    """
    Creates two files one with UTF-8 and the other with CP1252 encoding.
    It writes a random sequence of words, the order is reversed in the second file
    """
    
    generated_word_list = generate_words(word_count)

    with open('file1.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(generated_word_list))

    with open('file2.txt', 'w', encoding='CP1252') as f:
        # Use slicing to reverse the list
        f.write(', '.join(generated_word_list[::-1]))