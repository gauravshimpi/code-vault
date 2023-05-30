#!/bin/python3

def compare_triplets(a, b):
    alice = bob = 0
    for index in range(len(a)):
        if a[index] > b[index]:
            alice += 1
        elif a[index] < b[index]:
            bob += 1
    return [alice, bob]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)
    print(result)
