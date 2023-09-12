#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotate_left(d, arr):
    return arr[d:] + arr[:d]


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        d = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = rotate_left(d, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
