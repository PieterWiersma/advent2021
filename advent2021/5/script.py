"""

"""

input = [1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2]

class Fish():
    def __init__(self, timer):
        self.timer = timer

    def age(self):
        if self.timer == 0:
            self.timer = 6
            return True # spawn new fish

        self.timer -= 1
        return False # Don't spawn new fish

    def show(self):
        return self.timer


def ass_1():
    fish_list= []
    for i in input:
        fish_list.append(Fish(i))

    for i in range(80):
        #print('day: %s' % i)
        for fish in fish_list:
            if fish.age():
                fish_list.append(Fish(9))

    results = []
    for fish in fish_list:
        results.append(fish.show())

    #print(results)
    print(len(fish_list))


def ass_2():
    data = {}
    for i in range(11):
        data[i] = len([x for x in input if x == i])

    for step in range(256):
        for i in range(11):
            if i == 0:
                data[7] = data[i] + data[7]
                data[9] = data[i]
            else:
                data[i-1] = data[i]
        #print(data)

    print(sum(data.values()))

ass_1()
ass_2()
