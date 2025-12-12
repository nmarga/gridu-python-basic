"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def read_files(dir_path: str) -> None:
    """
    Reads all the file from a folder path.
    Creates an output file with the contents merged
    """

    # Save the contents of each file in a list
    file_contents = []

    file_paths = os.listdir(dir_path)

    # Sort by file name
    file_paths.sort()

    # Sort by length of the file name since .sort() is stable
    file_paths.sort(key = lambda x : len(x))

    # Iterate through each file name found in the dir_path sorted by characters
    for file_path in file_paths:

        # Open the file and append its content to the list
        with open(dir_path + '/' + file_path, 'r') as f:
            file_contents.append(f.read())
    
    # Join the list in a string output and write it to result.txt file
    with open('./result.txt', 'w') as f:
        f.write(', '.join(file_contents))