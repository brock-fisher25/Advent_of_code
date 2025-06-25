import os

os.chdir("C:\Documents\Personal\Github\Advent-of-code")

def read_file():
    file = open("input.txt", "r")
    return file

def fix_update(update, instruction_dict):
    fixed_update = []
    swapped = False
    for num in update:
        if swapped:
            fixed_update.append(num)
            continue
        if fixed_update == []:
            fixed_update.append(num)
            continue
        for i in range(len(fixed_update)):
            if fixed_update[i] in instruction_dict.keys() and num in instruction_dict[fixed_update[i]]:
                # if numbers are out of order, swap two numbers then return new list for future analysis
                temp_val = fixed_update[i]
                fixed_update[i] = num
                fixed_update.append(temp_val)
                swapped = True
                break
        if not swapped:
            fixed_update.append(num)
    return fixed_update, swapped

def corrected_updates(updates, instruction_dict):
    total = 0
    for update in updates:
        is_updating = True
        fixed_update = update.split(',')
        while is_updating:
            fixed_update, is_updating = fix_update(fixed_update, instruction_dict)
        total += int(fixed_update[len(fixed_update) // 2])

    return total

def solution_one():
    file = read_file()
    instructions = []
    updates = []
    total = 0
    for line in file:
        if '|' in line:
            instructions.append(line)
        elif ',' in line:
            updates.append(line)

    # create dictionary of instructions
    instruction_dict = {}
    for instruction in instructions:
        temp = instruction.split('|')
        if temp[1].strip() not in instruction_dict.keys():
            instruction_dict[temp[1].strip()] = [temp[0].strip()]
        else:
            instruction_dict[temp[1].strip()].append(temp[0].strip())
    for update in updates:
        valid_update = True
        temp = update.split(',')
        curr_update = []
        # loop through the update, checking that each new entry doesn't fall in the "must come after" list
        for num in temp:
            if curr_update == []:
                curr_update.append(num)
                continue
            for curr_num in curr_update:
                if curr_num in instruction_dict.keys():
                    if num in instruction_dict[curr_num]:
                        valid_update = False
                        break
            if not valid_update:
                break
            curr_update.append(num)
        if valid_update:
            total += int(curr_update[len(curr_update) // 2])
    return total

def solution_two():
    file = read_file()
    instructions = []
    updates = []
    total = 0
    for line in file:
        if '|' in line:
            instructions.append(line.strip())
        elif ',' in line:
            updates.append(line.strip())

    # create dictionary of instructions
    instruction_dict = {}
    incorrect_updates = []
    for instruction in instructions:
        temp = instruction.split('|')
        if temp[1].strip() not in instruction_dict.keys():
            instruction_dict[temp[1].strip()] = [temp[0].strip()]
        else:
            instruction_dict[temp[1].strip()].append(temp[0].strip())
    for update in updates:
        valid_update = True
        temp = update.split(',')
        curr_update = []
        # loop through the update, checking that each new entry doesn't fall in the "must come after" list
        for num in temp:
            if curr_update == []:
                curr_update.append(num)
                continue
            for curr_num in curr_update:
                if curr_num in instruction_dict.keys():
                    if num in instruction_dict[curr_num]:
                        valid_update = False
                        break
            if not valid_update:
                break
            curr_update.append(num)
        if not valid_update:
            incorrect_updates.append(update)
    return corrected_updates(incorrect_updates, instruction_dict)

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
