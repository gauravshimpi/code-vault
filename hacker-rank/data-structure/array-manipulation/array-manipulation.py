def array_manipulation(n, queries):
    array = [0]*(n+1)
    max_value = 0
    for start_index, end_index, value in queries:
        for i in range(start_index, end_index + 1):
            array[i] += value
        max_value = max(max_value, max(array))
    return max_value

def read_input(path):
    with open(path,'r') as fp:
        lines = fp.readlines()
        n, q = list(map(int,lines[0].rstrip().split()))
        del lines[0]
        queries = [list(map(int,line.rstrip().split())) for line in lines]
        return [int(n), q, queries]

if __name__ == '__main__':
    test_case_path = '/home/root155/Documents/all_projects/Training/code-vault/hacker-rank/data-structure/array-manipulation/test_case_04.txt'
    n,m, queries = read_input(test_case_path)

    result = array_manipulation(n, queries)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
