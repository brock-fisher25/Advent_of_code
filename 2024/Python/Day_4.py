import os

os.chdir("C:\Documents\Personal\Github\Advent-of-code")

def read_file():
    list = []
    file = open("input.txt", "r")
    for line in file:
        list.append(line)
    return list

def check_up(list, i, j):
    if i < 3:
        return 0
    if list[i-1][j] == 'M' and list[i-2][j] == 'A' and list[i-3][j] == 'S':
        return 1
    return 0

def check_down(list, i, j):
    if i >= len(list) - 3:
        return 0
    if list[i+1][j] == 'M' and list[i+2][j] == 'A' and list[i+3][j] == 'S':
        return 1
    return 0

def check_left(list, i, j):
    if j < 3:
        return 0
    if list[i][j-1] == 'M' and list[i][j-2] == 'A' and list[i][j-3] == 'S':
        return 1
    return 0

def check_right(list, i, j):
    if j >= len(list[i]) - 3:
        return 0
    if list[i][j+1] == 'M' and list[i][j+2] == 'A' and list[i][j+3] == 'S':
        return 1
    return 0

def check_up_left_diagonal(list, i, j):
    if i < 3 or j < 3:
        return 0
    if list[i-1][j-1] == 'M' and list[i-2][j-2] == 'A' and list[i-3][j-3] == 'S':
        return 1
    return 0

def check_up_right_diagonal(list, i, j):
    if i < 3 or j >= len(list[i]) - 3:
        return 0
    if list[i-1][j+1] == 'M' and list[i-2][j+2] == 'A' and list[i-3][j+3] == 'S':
        return 1
    return 0

def check_down_left_diagonal(list, i, j):
    if i >= len(list) - 3 or j < 3:
        return 0
    if list[i+1][j-1] == 'M' and list[i+2][j-2] == 'A' and list[i+3][j-3] == 'S':
        return 1
    return 0

def check_down_right_diagonal(list, i, j):
    if i >= len(list) - 3 or j >= len(list[i]) - 3:
        return 0
    if list[i+1][j+1] == 'M' and list[i+2][j+2] == 'A' and list[i+3][j+3] == 'S':
        return 1
    return 0

def solution_one():
    list = read_file()
    total = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 'X':
                total += check_up(list, i, j)
                total += check_down(list, i, j)
                total += check_left(list, i, j)
                total += check_right(list, i, j)
                total += check_up_left_diagonal(list, i, j)
                total += check_up_right_diagonal(list, i, j)
                total += check_down_left_diagonal(list, i, j)
                total += check_down_right_diagonal(list, i, j)
    return total

def solution_two():
    list = read_file()
    total = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 'A':
                if i < 1 or j < 1 or i >= len(list) - 1 or j >= len(list[i]) - 1:
                    continue
                # check up/left for m or s
                diag_one = False
                diag_two = False
                ms_one, ms_two = ['M','S'], ['M','S']
                if list[i-1][j-1] in ms_one:
                    # check bottom right for other letter
                    ms_one.remove(list[i-1][j-1])
                    if list[i+1][j+1] in ms_one:
                        diag_one = True
                # check down/left for m or s
                if list[i+1][j-1] in ms_two:
                    # check top right for other letter
                    ms_two.remove(list[i+1][j-1])
                    if list[i-1][j+1] in ms_two:
                        diag_two = True
                if diag_one and diag_two:
                    total += 1
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
