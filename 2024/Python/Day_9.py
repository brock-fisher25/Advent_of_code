import copy

def read_file():
    file = open("input_day_9.txt", "r")
    return file.read()

def find_next_num(num_list, j):
    # get last index of a number
    for x in range(j, -1, -1):
        if num_list[x] != '.':
            j = x
            break
    return j

# def process_num_list(num_list, j):
#     # get count of same number
#     count = 1
#     num = num_list[j]
#     for i in range(j-1, -1, -1):
#         if num_list[i] == num_list[j]:
#             count += 1
#         else:
#             break
#     # search num_list from the start to see if there is a spot we can put the group of numbers
#     done = False
#     list_len = j - count
#     check_count = 0
#     for i in range(list_len + 1):
#         if num_list[i] == '.':
#             check_count += 1
#             # checks to see if count only has one
#             if check_count == count:
#                 num_list[i] = num
#                 num_list[j] = '.'
#                 break
#             for k in range(i+1, list_len + 1):
#                 if num_list[k] == '.':
#                     check_count += 1
#                     if check_count == count:
#                         for l in range (i, i + count):
#                             num_list[l] = num
#                         for m in range(j, list_len, -1):
#                             num_list[m] = '.'
#                         done = True
#                 else:
#                     check_count = 0
#                     break
#                 if done:
#                     break
#             if done:
#                 break
#     return num_list, j - count


def solution_one():
    file = read_file()
    instruction_list = []
    free_space = False
    id = 0
    for char in file:
        if free_space:
            instruction_list.extend(['.'] * int(char))
            free_space = False
        else:
            instruction_list.extend([str(id)] * int(char))
            free_space = True
            id += 1
    i = 0
    num_list = copy.deepcopy(instruction_list)
    j = find_next_num(num_list, len(num_list) -1)
    while i < len(instruction_list) and i < j:
        if num_list[i] == '.':
            num_list[i] = num_list[j]
            num_list[j] = '.'
            j = find_next_num(num_list, j)
        i += 1
    total = 0
    for index in range(len(num_list)):
        if num_list[index]== '.':
            continue
        total += int(num_list[index]) * index
    return total

# def solution_two():
#     file = read_file()
#     instruction_list = []
#     free_space = False
#     id = 0
#     for char in file:
#         if free_space:
#             instruction_list.extend(['.'] * int(char))
#             free_space = False
#         else:
#             instruction_list.extend([str(id)] * int(char))
#             free_space = True
#             id += 1
#     num_list = copy.deepcopy(instruction_list)
#     moved_ids = []
#     j = len(instruction_list) - 1
#     while j > 0:
#         if num_list[j] != '.':
#             if num_list[j] in moved_ids:
#                 j -= 1
#                 continue
#             moved_ids.append(num_list[j])
#             num_list, j = process_num_list(num_list, j)
#         else:
#             j -= 1
#     total = 0
#     for index in range(len(num_list)):
#         if num_list[index]== '.':
#             continue
#         total += int(num_list[index]) * index
#     return total

def solution_two():
    file = read_file()
    free_space_list = []
    id_list = []
    free_space = False
    id = 0
    pos = 0
    for char in file:
        if free_space:
            free_space_list.append(['.', pos, int(char)])
            free_space = not free_space
            pos += int(char)
        else:
            id_list.append([id, pos, int(char)])
            free_space = not free_space
            id += 1
            pos += int(char)
    # check to see in reverse order if the entry at the id list can move to the left
    id_list.reverse()
    for list in id_list:
        for free_list in free_space_list:
            if free_list[2] >= list[2] and free_list[1] < list[1]:
                list[1] = free_list[1]
                free_list[1] += list[2]
                free_list[2] -= list[2]
                break 
    total = 0
    for list in id_list:
        for _ in range(list[2]):
            total += (list[0] * list[1])
            list[1] += 1
    return total




if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two) #6349492251099 is correct answer
