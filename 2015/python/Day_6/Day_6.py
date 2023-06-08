def read_text_file():
    with open('Day_6_input.txt') as file:
        return file.readlines()
    
def toggle(map, first_instruction, second_instruction, state):
    first_set = first_instruction.split(',')
    second_set = second_instruction.split(',')
    first_set = [eval(i) for i in first_set]
    second_set = [eval(i) for i in second_set]
    for i in range(first_set[0], second_set[0] + 1):
        for j in range(first_set[1], second_set[1] + 1):
            if state == 'off':
                map[i][j] = 0
            elif state == 'on':
                map[i][j] = 1
            else:
                map[i][j] = not map[i][j]
    return map

def first_part():
    map = [[0] * 1000] *1000
    instructions = read_text_file()
    counter = 0
    for instruction in instructions:
        instruction_list = instruction.split(' ')
        if instruction_list[1] == 'off':
            map = toggle(map, instruction_list[2], instruction_list[-1], 'off')
        elif instruction_list[1] == 'on':
            map = toggle(map, instruction_list[2], instruction_list[-1], 'on')
        else:
            map = toggle(map, instruction_list[1], instruction_list[-1], 'toggle')
        counter += 1
        if counter > 9:
            break
    total_lights = 0
    for i in map:
        for j in i:
            if j == 1:
                total_lights += 1
    return total_lights


def second_part():
    return

if __name__ == "__main__":
    print(first_part()) #returns 322000 is too low
    print(second_part()) #returns 69