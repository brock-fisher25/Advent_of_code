def read_file():
    file = open("input_day_13.txt", "r")
    return file

def solution_one():
    file = read_file()
    button_a = []
    button_b = []
    prize = []
    total = 0
    for line in file:
        if 'Button A' in line:
            temp = line.split('+')
            button_a.append(int(temp[1].split(',')[0]))
            button_a.append(int(temp[-1].strip()))
        elif 'Button B' in line:
            temp = line.split('+')
            button_b.append(int(temp[1].split(',')[0]))
            button_b.append(int(temp[-1].strip()))
        elif 'Prize' in line:
            temp = line.split('=')
            prize.append(int(temp[1].split(',')[0]))
            prize.append(int(temp[-1].strip()))
        if prize != []:
            # equation 1: (x * button_a[0]) + (y * button_b[0]) = prize[0]
            # equation 1: (x * a1) + (y * b1) = c1
            # equation 2: (x * button_a[1]) + (y * button_b[1]) = prize[1]
            # equation 2: (x * a2) + (y * b2) = c2
            x = ((prize[0] * button_b[1]) - (prize[1] * button_b[0])) / ((button_a[0] * button_b[1]) - (button_a[1] * button_b[0]))
            y = ((prize[1] * button_a[0]) - (prize[0] * button_a[1])) / ((button_a[0] * button_b[1]) - (button_a[1] * button_b[0]))
            if x < 101 and y < 101:
                if x.is_integer() and y.is_integer():
                    total += (3 * int(x)) + int(y)
            button_a = []
            button_b = []
            prize = []
    return total
def solution_two():
    file = read_file()
    button_a = []
    button_b = []
    prize = []
    total = 0
    for line in file:
        if 'Button A' in line:
            temp = line.split('+')
            button_a.append(int(temp[1].split(',')[0]))
            button_a.append(int(temp[-1].strip()))
        elif 'Button B' in line:
            temp = line.split('+')
            button_b.append(int(temp[1].split(',')[0]))
            button_b.append(int(temp[-1].strip()))
        elif 'Prize' in line:
            temp = line.split('=')
            prize.append(int(temp[1].split(',')[0]) + 10000000000000)
            prize.append(int(temp[-1].strip()) + 10000000000000)
        if prize != []:
            # equation 1: (x * button_a[0]) + (y * button_b[0]) = prize[0]
            # equation 1: (x * a1) + (y * b1) = c1
            # equation 2: (x * button_a[1]) + (y * button_b[1]) = prize[1]
            # equation 2: (x * a2) + (y * b2) = c2
            x = ((prize[0] * button_b[1]) - (prize[1] * button_b[0])) / ((button_a[0] * button_b[1]) - (button_a[1] * button_b[0]))
            y = ((prize[1] * button_a[0]) - (prize[0] * button_a[1])) / ((button_a[0] * button_b[1]) - (button_a[1] * button_b[0]))
            if x.is_integer() and y.is_integer():
                total += (3 * int(x)) + int(y)
            button_a = []
            button_b = []
            prize = []
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
