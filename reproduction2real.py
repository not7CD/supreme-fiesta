import re
import csv

"""Module to format reproduced csv files from pdf"""


def format_row(list_of_strings):
    """ joining firstname and lastname in one column """
    # regex to find `(7-14)`, `(22-4)` and other
    custom_hour_pattern = r'[\(]\d+\D\d+[\)]'

    # Get list of known names locations
    fullnames_in_row = list(zip(list_of_strings[1::3], list_of_strings[2::3]))
    # Join first and last name with space if there is empty string, join with
    # no space
    fullnames_in_row = [' '.join([a, b]) if (
        a and b) else a + b for a, b in fullnames_in_row]
    # print(fullnames_in_row)
    # Get list of known custom hours locations
    custom_hour_in_row = list_of_strings[3::3]
    # Find all custom hours
    custom_hour_in_row = [re.search(custom_hour_pattern, value)
                          for value in custom_hour_in_row]

    fullnames_in_row = list(zip(fullnames_in_row, custom_hour_in_row))
    fullnames_in_row = list(map(
        lambda x: x[0] + ' ' + x[1].group(0) if x[1] != None else x[0], fullnames_in_row))
    # [value for value in custom_hour_in_row if value not None]

    other_values_in_row = [re.sub(custom_hour_pattern, '', value)
                           for value in list_of_strings[0::3]]
    # print(other_values_in_row)
    # https://stackoverflow.com/questions/3678869/pythonic-way-to-combine-two-lists-in-an-alternating-fashion
    formated_list_of_strings = [None] * \
        (len(fullnames_in_row) + len(other_values_in_row))
    formated_list_of_strings[::2] = other_values_in_row
    formated_list_of_strings[1::2] = fullnames_in_row
    # print(formated_list_of_strings)
    return formated_list_of_strings


def format_file():
    """format whole file row by row"""

    with open('data/raw/grafik.csv', 'r') as csvrawfile:
        raw_file = csv.reader(csvrawfile)
        with open('data/formated/grafik.csv', 'w') as csvformatedfile:
            formated_file = csv.writer(csvformatedfile, quoting=csv.QUOTE_MINIMAL)
            for row in raw_file:
                formated_file.writerow(format_row(row))

if __name__ == '__main__':
    format_file()
