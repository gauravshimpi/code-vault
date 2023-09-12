"""
@Author: Gaurav Shimpi
@Date: 28th July, 2023
"""


def find_sub_string_occurrence(input_string: str) -> dict:
    """
    finds sub string and their occurrence.
    :param input_string: string form which unique words needs to be extracted.
    :return: dictionary with words and their occurrence.
    """
    # Store occurrence
    sub_string_occurrence = {}
    # Extracting words from input string.
    words = input_string.split()
    for word in words:
        # Record unique words and their occurrence.
        sub_string_occurrence[word] = sub_string_occurrence.get(word, 0) + 1
    # Sort the unique words in descending order.
    sorted_data = dict(sorted(sub_string_occurrence.items(), key=lambda x: x[1], reverse=True))
    return sorted_data


if __name__ == '__main__':
    my_string = input("Enter string: ")
    result = find_sub_string_occurrence(my_string)
    print(result)
