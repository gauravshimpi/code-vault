"""
@Author: Gaurav Shimpi
@Date: 28th July, 2023
"""


def find_most_frequent_number(input_list: iter) -> int:
    """
    finds sub string and their occurrence.
    :param input_list: string form which unique words needs to be extracted.
    :return: dictionary with words and their occurrence.
    """
    print(input_list.count.str)
    most = max(set(input_list), key=input_list.count)
    print(most)


if __name__ == '__main__':
    my_list = [1,1,1,7,5,7,8,9,0,5,3,10]
    result = find_most_frequent_number(my_list)
    print(result)
