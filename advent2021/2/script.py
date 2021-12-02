"""

"""


class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0

    def move(self, direction, steps):
        if direction == 'forward':
            self.horizontal += steps
        elif direction == 'down':
            self.depth += steps
        elif direction == 'up':
            self.depth -= steps

    def show(self):
        print('depth: %s' % self.depth)
        print('horizontal: %s' % self.horizontal)
        product = self.depth * self.horizontal
        print('product: %s' % product)



class AdvancedSubmarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def move(self, direction, steps):
        if direction == 'forward':
            self.horizontal += steps
            self.depth += steps * self.aim
        elif direction == 'down':
            self.aim += steps
        elif direction == 'up':
            self.aim -= steps


    def show(self):
        print('depth: %s' % self.depth)
        print('horizontal: %s' % self.horizontal)
        product = self.depth * self.horizontal
        print('product: %s' % product)



def get_input(file):
    input = open(file, 'r').readlines()
    input = [x.replace('\n', '') for x in input]
    input = [x.split(' ') for x in input]
    input = [[x[0], int(x[1])] for x in input]
    return input


def assignment_1():
    input = get_input('input.txt')
    sub = Submarine()
    for line in input:
        sub.move(line[0], line[1])
    sub.show()


def assignment_2():
    input = get_input('input.txt')
    sub = AdvancedSubmarine()
    for line in input:
        sub.move(line[0], line[1])
    sub.show()


assignment_2()
