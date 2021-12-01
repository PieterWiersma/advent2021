"""

"""


def get_input(file):
    input = open(file, 'r').readlines()
    return [int(x.replace('\n', '')) for x in input]


def assignment_1(input):
    #input = get_input('input.txt')
    result = []
    for i in range(1, len(input)):
        result.append([input[i], input[i] - input[i-1]])

    print(sum([x[1] > 0 for x in result]))


def assignment_2():
    input = get_input('input.txt')
    result = []
    for i in range(2, len(input)):
        value = input[i-2] + input[i-1] + input[i]
        result.append(value)

    assignment_1(result)


assignment_2()
