def read_file():
    file = open('input.txt', 'r')
    return file

def find_digit(length, start_index, offset, line):
    digit = 0
    index = 0
    for i in range(start_index, length - offset):
        if int(line[i]) > digit:
            digit = int(line[i])
            index = i
    return [digit, index + 1]


def solution_one():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
        first = 0
        first_index = 0
        second = 0
        for i in range(len(line) - 1):
            if int(line[i]) > first:
                first = int(line[i])
                first_index = i
        for i in range(first_index + 1, len(line)):
            if int(line[i]) > second:
                second = int(line[i])
        joltage = first * 10 + second
        sum = sum + joltage
    return sum
    
def solution_two():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
        digits = [0] * 12
        indexes = [0] * 12
        offset = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        for i in range(len(digits)):
            if i == 0:
                temp = find_digit(len(line), indexes[i], offset[i], line)
            else:
                temp = find_digit(len(line), indexes[i - 1], offset[i], line)
            digits[i] = temp[0]
            indexes[i] = temp[1]
        joltage = int("".join(map(str, digits)))
        sum = sum + joltage
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
