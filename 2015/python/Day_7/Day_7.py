# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
# 
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
#
# For example:
#
# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
#
# For example, here is a simple circuit:
#
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:
#
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
#
# Your puzzle answer was 956.
# 
# --- Part Two ---
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
#
# Your puzzle answer was 40149.
#
# Both parts of this puzzle are complete! They provide two gold stars: **
#--------------------------------------------------------------------------------------------------------------------------------------------

def read_text_file():
    with open('Day_7_input.txt') as file:
        return file.readlines()

def read_instructions(wires, wires_length, instructions):
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
    return wires

def first_part():
    instructions = read_text_file()
    wires = {}
    wires_length = 0
    for instruction in instructions:
        temp = instruction.split('->')
        wires[temp[1].strip()] = ''
        wires_length += 1

    wires = read_instructions(wires, wires_length, instructions)
    return wires['a']

def second_part():
    instructions = read_text_file()
    wires = {}
    wires_length = 0
    for instruction in instructions:
        temp = instruction.split('->')
        if temp[1].strip() == 'b':
            wires['b'] = first_part()
            instructions[wires_length] = str(first_part()) + ' -> b\n'
            wires_length += 1
            continue
        wires[temp[1].strip()] = ''
        wires_length += 1
    wires = read_instructions(wires, wires_length, instructions)
    return wires['a']

if __name__ == "__main__":
    print(first_part()) #returns 956
    print(second_part()) #returns 40149