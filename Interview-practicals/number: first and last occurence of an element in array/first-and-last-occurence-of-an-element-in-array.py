def find_first_last_index(my_list, target, first):
    low = 0
    curr_element = -1
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] < target:
            low = mid + 1
        elif my_list[mid] > target:
            high = mid - 1

        else:
            curr_element = mid
            if first:
                high = mid - 1
            else:
                low = mid + 1
    return curr_element


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
    target = 4
    result = find_first_last_index(my_list, target, True)
    print(result)
