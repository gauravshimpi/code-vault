def string_manipulation(input_string, size):
    sub_string_occurrence = {}
    for index in range(len(input_string) - size + 1):
        sub_string = input_string[index:index + size]
        sub_string_occurrence[sub_string] = sub_string_occurrence.get(sub_string, 0) + 1
    return sub_string_occurrence


def read_input(path):
    with open(path, 'r') as fp:
        lines = fp.readlines()
        input_string = lines[0].strip()
        size = int(lines[1].strip())
        return input_string, size


if __name__ == '__main__':
    test_case_path = 'test_case_02.txt'
    my_string, my_size = read_input(test_case_path)

    result = string_manipulation(my_string, my_size)
    print(result)