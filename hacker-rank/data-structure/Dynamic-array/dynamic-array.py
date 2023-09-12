#!/bin/python3

import os


def dynamic_array(n, queries):
    last_answer = 0
    arr = [[] for _ in range(n)]
    ans_arr = []
    for query in queries:
        query_type, x, y = query
        idx = ((x ^ last_answer) % n)
        if query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            last_answer = arr[idx][y % len(arr[idx])]
            ans_arr.append(last_answer)
    return ans_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[a1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamic_array(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
