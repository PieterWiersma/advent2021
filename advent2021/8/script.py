


def get_input(file):
    input = open(file, 'r').readlines()
    input = [x.replace('\n', '') for x in input]
    input = [x.split('|') for x in input]
    input = [[x[0].strip().split(' '), x[1].strip().split(' ')] for x in input]
    return input


def ass_1(input):
    counter = 0
    no_of_interest = [2,3,4,7]
    for line in input:
        for item in line[0]:
            if len(item) in no_of_interest:
                counter += 1
    print(counter)


def translate_str(mapping, input_str):
    for key, value in mapping.items():
        if len(value) == len(input_str) == len(set([x for x in value]) & set([x for x in input_str])):
            return key


def generate_mapping(input):
    mapping = {}
    mapping[1] = [x for x in input if len(x) == 2][0]
    mapping[8] = [x for x in input if len(x) == 7][0]
    mapping[7] = [x for x in input if len(x) == 3][0]
    mapping[4] = [x for x in input if len(x) == 4][0]
    for key in input:
        if len(key) == 6: # 0, 6, 9
            if len(set([x for x in key]) & set([x for x in mapping[4]])) == 4:
                mapping[9] = key
            elif len(set([x for x in key]) & set([x for x in mapping[1]])) == 2:
                mapping[0] = key
            else:
                mapping[6] = key

    for key in input: # double cuz im lazy
        if len(key) == 5: # 2, 3, 5
            if len(set([x for x in key]) & set([x for x in mapping[1]])) == 2:
                mapping[3] = key
            elif len(set([x for x in key]) & set([x for x in mapping[9]])) == 5:
                mapping[5] = key
            else:
                mapping[2] = key

    return mapping


def ass_2():
    input = get_input('input.txt')
    all_numbers = []
    for line in input:
        number_bin = []
        mapping = generate_mapping(line[0])
        for item in line[1]:
            number_bin.append(translate_str(mapping, item))

        all_numbers.append(int(''.join([str(x) for x in number_bin])))
    print(sum(all_numbers))

ass_2()
