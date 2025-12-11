def read_file():
    file = open('input.txt', 'r')
    return file

def fewest_presses(lights, buttons, final_lights):
    if lights == final_lights:
        return 

def solution_one():
    file = read_file()
    sum = 0
    buttons = []
    lights = []
    final_lights = []
    for line in file:
        line = line.strip()
        tmp = line.split(' ')
        for i in tmp:
            if i[0] == '[':
                new_lights = []
                final_lights = list(i[1:len(i)-1])
                for j in range(len(i) - 2):
                    new_lights.append('.')
                lights.append(new_lights)
            elif i[0] == '(':
                buttons.append([i[1:len(i)-1]])
        sum += fewest_presses(lights, buttons, final_lights)
        exit()
    return sum

def solution_two():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
