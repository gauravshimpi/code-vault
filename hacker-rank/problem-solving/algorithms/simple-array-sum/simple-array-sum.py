#!/bin/python3

import os


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simple_array_sum(ar):
    # method 1: using builtin sum function
    # output_sum = sum(ar)

    # method 2: simple for loop using indexing(range)
    # output_sum = 0
    # for i in range(len(ar)):
    #     output_sum += ar[i]

    output_sum = 0
    for ele in ar:
        output_sum += ele

    return output_sum


if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    print(result)
