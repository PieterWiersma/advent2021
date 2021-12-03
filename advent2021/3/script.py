"""

"""


def get_input(file):
    input = open(file, 'r').readlines()
    input = [x.replace('\n', '') for x in input]
    return input


def transform_input_ass1(input):
    #breakpoint()
    length = len(input[0])
    new_list = []
    for i in range(length):
        tmp_container = []
        for item in input:
            tmp_container.append(int(item[i]))
        new_list.append(tmp_container)
    return new_list


def find_most_frequent_number(list_of_no):
    avg = sum([int(x) for x in list_of_no])/len(list_of_no)
    if avg < 0.5:
        return 0
    else:
        return 1


def find_least_frequent_number(list_of_no):
    avg = sum([int(x) for x in list_of_no])/len(list_of_no)
    if avg <= 0.5:
        return 1
    else:
        return 0


def solve_ass1(input):
    solution_bin1 = []
    solution_bin2 = []
    for item in input:
        solution_bin1.append(find_most_frequent_number(item))

    for item in input:
        solution_bin2.append(find_least_frequent_number(item))

    bin1 = int(''.join([str(x) for x in solution_bin1]), 2)
    bin2 = int(''.join([str(x) for x in solution_bin2]), 2)

    #print('bin1: %s, bin2: %s, product: %s' %(bin1, bin2, bin1*bin2))

    return ''.join([str(x) for x in solution_bin1])


def ass2_part1(input):
    for i in range(len(input[0])):
        bin1 = solve_ass1(transform_input_ass1(input))
        input = [x for x in input if x[i] == bin1[i]]
        if len(input) == 1:
            return input
    return input


def ass2_part2(input):
    #breakpoint()
    for i in range(len(input[0])):
        bin1 = solve_ass1(transform_input_ass1(input))
        input = [x for x in input if x[i] != bin1[i]]
        if len(input) == 1:
            print(input)
            return input
    return input



if __name__ == "__main__":
    original_input = get_input('input.txt')
    original_input_copy = [x for x in original_input]

    x = ass2_part1(original_input)
    y = ass2_part2(original_input_copy)
    print(int(x[0],2))
    print(int(y[0],2))
    print(int(x[0],2) * int(y[0],2))
