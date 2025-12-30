def read_text_file():
    with open('Day_6_input.txt') as file:
        return file.readlines()
    
def toggle(map, first_instruction, second_instruction, state):
    first_set_coordinates = first_instruction.split(',')
    second_set_coordinates = second_instruction.split(',')
    first_set_coordinates = [eval(i) for i in first_set_coordinates]
    second_set_coordinates = [eval(i) for i in second_set_coordinates]
    for i in range(first_set_coordinates[0], second_set_coordinates[0] + 1):
        for j in range(first_set_coordinates[1], second_set_coordinates[1] + 1):
            if state == 'off':
                map[i][j] = 0
            elif state == 'on':
                map[i][j] = 1
            else:
                map[i][j] = not map[i][j]
    return map

def first_part():
    map = [[0 for i in range(1000)] for row in range(1000)]
    instructions = read_text_file()
    for instruction in instructions:
        instruction_list = instruction.split(' ')
        if instruction_list[1] == 'off':
            map = toggle(map, instruction_list[2], instruction_list[-1], 'off')
        elif instruction_list[1] == 'on':
            map = toggle(map, instruction_list[2], instruction_list[-1], 'on')
        else:
            map = toggle(map, instruction_list[1], instruction_list[-1], 'toggle')
    total_lights = 0
    for i in map:
        for j in i:
            if j == 1:
                total_lights += 1
    return total_lights

def brightness(map, first_instruction, second_instruction, brightness_change):
    first_set_coordinates = first_instruction.split(',')
    second_set_coordinates = second_instruction.split(',')
    first_set_coordinates = [eval(i) for i in first_set_coordinates]
    second_set_coordinates = [eval(i) for i in second_set_coordinates]
    for i in range(first_set_coordinates[0], second_set_coordinates[0] + 1):
        for j in range(first_set_coordinates[1], second_set_coordinates[1] + 1):
            map[i][j] += brightness_change
            if map[i][j] < 0:
                map[i][j] = 0
    return map


def second_part():
    map = [[0 for i in range(1000)] for row in range(1000)]
    instructions = read_text_file()
    for instruction in instructions:
        instruction_list = instruction.split(' ')
        if instruction_list[1] == 'off':
            map = brightness(map, instruction_list[2], instruction_list[-1], -1)
        elif instruction_list[1] == 'on':
            map = brightness(map, instruction_list[2], instruction_list[-1], 1)
        else:
            map = brightness(map, instruction_list[1], instruction_list[-1], 2)
    total_brightness = 0
    for i in map:
        for j in i:
            total_brightness += j
    return total_brightness

if __name__ == "__main__":
    print(first_part()) #returns 322000 is too low
    print(second_part()) #returns 15343601
