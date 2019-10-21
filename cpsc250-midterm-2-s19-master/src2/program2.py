"""
Program 2 Module defines 1 function that loads a text file

Don't forget your required import statements
@author Elijah Weske
"""
import os


def search_text_data(file_path, word):
    """
    Load data from a text file and return the total occurrence of the word
    :param file_path: fully qualified file path (directory and file name with extension)
    :param word: string to be searched
    :return: occurrence of the word
    """

    count = 0

    check_path = os.path.isfile(file_path)

    if check_path:
        with open(file_path, 'r') as my_file:
            for row in my_file:
                if word in row:
                    count += 1
    else:
        count = -1
        
    return count