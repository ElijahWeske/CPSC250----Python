"""
Program 1 Module defines 1 function that loads a CSV file
@author Elijah Weske
"""
import csv  # Might come in handy


# --------------------------------------------------------------------------------------------
# load_csv
# --------------------------------------------------------------------------------------------
def load_csv(file_path):
    """
    Load data from comma separated value text file with 3 separate columns delimited by commas,
    e.g.
    0,0.0,1.0

    Return as 3 separate lists of numbers
    The first column is integer, the other two are floating point values
    :param file_path: fully qualified file path (directory and file name with extension)
    :return: col0, col1, col2 lists
    """

    col0 = []
    col1 = []
    col2 = []

    with open(file_path, 'r') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')

        for row in file_reader:
            col0.append(float(row[0]))
            col1.append(float(row[1]))
            col2.append(float(row[2]))

    return col0, col1, col2



