#!/bin/python3


def a_very_big_sum(ar):
    # method 1: using inbuilt sum function
    # return sum(ar)

    output_sum = 0
    for ele in ar:
        output_sum += ele
    return output_sum


if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(ar)

    print(result)
