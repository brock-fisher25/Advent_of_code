def read_file():
    file = open('input.txt', 'r')
    return file

def check_roll(input_map, i, j):
    if input_map[i][j] == '@':
        return 1
    return 0

def check_above(input_map, i, j):
    if i == 0:
        return 0
    return check_roll(input_map, i - 1, j)

def check_below(input_map, i, j):
    if i == len(input_map) - 1:
        return 0
    return check_roll(input_map, i + 1, j)

def check_left(input_map, i, j):
    if j == 0:
        return 0
    return check_roll(input_map, i, j - 1)

def check_right(input_map, i, j):
    if j == len(input_map[0]) - 1:
        return 0
    return check_roll(input_map, i, j + 1)

def check_tlcorner(input_map, i,j):
    if i == 0 or j == 0:
        return 0
    return check_roll(input_map, i - 1, j - 1)

def check_trcorner(input_map, i, j):
    if i == 0 or j == len(input_map[0]) - 1:
        return 0
    return check_roll(input_map, i - 1, j + 1)

def check_blcorner(input_map, i, j):
    if i == len(input_map) - 1 or j == 0:
        return 0
    return check_roll(input_map, i + 1, j - 1)

def check_brcorner(input_map, i, j):
    if i == len(input_map) - 1 or j == len(input_map[0]) - 1:
        return 0
    return check_roll(input_map, i + 1, j + 1)

def solution_one():
    file = read_file()
    sum = 0
    counter = 0
    input_map = []
    for line in file:
        line = line.strip()
        input_map.append([])
        for char in line:
            input_map[counter].append(char)
        counter = counter + 1
    for i in range(len(input_map)):
        for j in range(len(input_map[i])):
            count = 0
            if input_map[i][j] == '@':
                count = check_above(input_map, i, j) + check_below(input_map, i, j) + check_left(input_map, i, j) + check_right(input_map, i, j) + check_tlcorner(input_map, i, j) + check_trcorner(input_map, i, j) + check_blcorner(input_map, i, j) + check_brcorner(input_map, i, j)
                if count < 4:
                    sum = sum + 1
    return sum
    
def solution_two():
    file = read_file()
    sum = 0
    counter = 0
    input_map = []
    for line in file:
        line = line.strip()
        input_map.append([])
        for char in line:
            input_map[counter].append(char)
        counter = counter + 1
    while True:
        removed = False
        for i in range(len(input_map)):
            for j in range(len(input_map[i])):
                count = 0
                if input_map[i][j] == '@':
                    count = check_above(input_map, i, j) + check_below(input_map, i, j) + check_left(input_map, i, j) + check_right(input_map, i, j) + check_tlcorner(input_map, i, j) + check_trcorner(input_map, i, j) + check_blcorner(input_map, i, j) + check_brcorner(input_map, i, j)
                    if count < 4:
                        removed = True
                        sum = sum + 1
                        input_map[i][j] = '.'
        if removed:
            continue
        else:
            break
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)