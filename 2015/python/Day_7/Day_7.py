def read_text_file():
    with open('Day_7_input.txt') as file:
        return file.readlines()

def first_part():
    instructions = read_text_file()
    wires = {}
    wires_length = 0
    for instruction in instructions:
        temp = instruction.split('->')
        wires[temp[1].strip()] = ''
        wires_length += 1

    value_list = wires.values()
    counter = 0
    while '' in value_list:
        instruction = instructions[counter].split('->')
        if 'NOT' in instruction[0].strip():
            temp = instruction[0].strip().split(' ')
            if wires[temp[1].strip().strip()] != '':
                wires[instruction[1].strip()] = ~int(wires[temp[1].strip()])
        elif 'OR' in instruction[0].strip():
            temp = instruction[0].strip().split(' ')
            if wires[temp[0].strip()] != '' and wires[temp[2].strip()] != '':
                wires[instruction[1].strip()] = int(wires[temp[0].strip()]) | int(wires[temp[2].strip()])
        elif 'AND' in instruction[0].strip():
            temp = instruction[0].strip().split(' ')
            if temp[0].strip() == '1':
                if wires[temp[2].strip()] != '':
                    wires[instruction[1].strip()] = int(temp[0].strip()) & int(wires[temp[2].strip()])
            else:
                if wires[temp[0].strip()] != '' and wires[temp[2].strip()] != '':
                    wires[instruction[1].strip()] = int(wires[temp[0].strip()]) & int(wires[temp[2].strip()])
        elif 'RSHIFT' in instruction[0].strip():
            temp = instruction[0].strip().split(' ')
            if wires[temp[0].strip()] != '':
                wires[instruction[1].strip()] = int(wires[temp[0].strip()]) >> int(temp[2].strip())
        elif 'LSHIFT' in instruction[0].strip():
            temp = instruction[0].strip().split(' ')
            if wires[temp[0].strip()] != '':
                wires[instruction[1].strip()] = int(wires[temp[0].strip()]) << int(temp[2].strip())
        else:
            if instruction[0].strip().strip().isnumeric():
                wires[instruction[1].strip()] = int(instruction[0].strip())
            else:
                if wires[instruction[0].strip()] != '':
                    wires[instruction[1].strip()] = wires[instruction[0].strip()]
        counter += 1
        value_list = wires.values()
        if counter == wires_length:
            counter = 0
    return wires['a']

def second_part():

    return

if __name__ == "__main__":
    print(first_part()) #returns 956
    print(second_part()) #