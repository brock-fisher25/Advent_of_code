def read_file():
    file = open("input.txt", "r")
    return file.read()

def find_next_char(char_list, j):
    # get last index of a number
    for x in range(j, -1, -1):
        if char_list[x] != '.':
            j = x
            break
    return j

# issue is numbers are overflowing a single char, so need to figure out how to store numbers themselves in the array
def solution_one():
    file = read_file()
    instruction_string = ''
    free_space = False
    id = 0
    for char in file:
        if free_space:
            instruction_string += '.' * int(char)
            free_space = False
        else:
            instruction_string += str(id) * int(char)
            free_space = True
            id += 1
    i = 0
    print(instruction_string)
    char_list = list(instruction_string)
    j = find_next_char(char_list, len(char_list) -1)
    while i < len(instruction_string) and i < j:
        if char_list[i] == '.':
            char_list[i] = char_list[j]
            char_list[j] = '.'
            j = find_next_char(char_list, j)
        i += 1
    total = 0
    print(''.join(char_list))
    for index in range(len(char_list)):
        if char_list[index]== '.':
            continue
        total += int(char_list[index]) * index
    return total

def solution_two():
    return 0




if __name__ == '__main__':
    answer_one = solution_one() ##115870332735 was too low
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
