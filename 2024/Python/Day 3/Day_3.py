import os

os.chdir("C:\Documents\Personal\Github\Advent-of-code")

def read_file():
    file = open("input.txt", 'r')
    return file

def process_string(string):
    x, y = 0, 0
    temp = string.split(',')
    if len(temp) < 2:
        return 0
    if temp[0].isdigit() and len(temp[0]) <= 3:
        x = int(temp[0])
    # second space contains a number, just have to figure out how big it is and if it has a ) at the end
    if temp[1][0].isdigit():
        y_string = temp[1][0]
        for i in range(1, len(temp[1])):
            if temp[1][i].isdigit() and len(y_string) < 3:
                y_string += temp[1][i]
            elif temp[1][i] == ')':
                y_string += temp[1][i]
                break
            # if anything else is found, invalid string
            else:
                return 0

        y = int(y_string[0:-1])
    return x * y


def solution_one():
    file = read_file()
    total = 0
    for line in file:
        temp = list(line.split('mul('))
        for string in temp:
            # if digit is in first slot (0), process string
            if len(string) == 0:
                continue
            if string[0].isdigit():
                total += process_string(string)

    return total

def solution_two():
    file = read_file()
    total = 0
    process_initial = True
    for line in file:
        # split string on each valid don't instruction to break up instructions
        temp = list(line.split("don't()"))
        for string in temp:
            # always count first batch of instructions
            if process_initial:
                process_initial = False
                initial_strings = list(temp[0].split('mul('))
                for initial in initial_strings:
                    if len(initial) == 0:
                        continue
                    if initial[0].isdigit():
                        total += process_string(initial)
                continue
            # split each don't instruction on every do instruction, to get instructions that should be counted
            if 'do()' in string:
                temp_2 = list(string.split('do()'))
                # skip first one as those instructions shouldn't be followed as they proceed the latest don't
                for i in range(1, len(temp_2)):
                    process_strings = list(temp_2[i].split('mul('))
                    for substring in process_strings:
                        if len(substring) == 0:
                            continue
                        if substring[0].isdigit():
                            total += process_string(substring)

    return total
    
if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
