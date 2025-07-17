def read_file():
    file = open("input.txt", "r")
    return file.read().split()

def process_stone(stone, stone_dict):
    if stone in stone_dict:
        return stone_dict[stone]
    
    if stone == '0':
        result = ('1', None)
    elif len(stone) % 2 == 0:
        first_stone = stone[:len(stone)//2]
        second_stone = str(int(stone[len(stone)//2:]))
        result = (first_stone, second_stone)
    else:
        result = (str(int(stone) * 2024), None)
    stone_dict[stone] = result
    return result
# [occurences of stone, stone_count]
def process_stones(stone, stone_dict, stone_count, blinks):
    if (stone, blinks) in stone_dict:
        stone_dict[(stone, blinks)][0] += 1
        return stone_dict, stone_count
    if blinks == 0:
        return stone_dict, (stone_count + 1)
    
    blinks -= 1
    if stone == '0':
        stone = '1'
        stone_dict, stone_count = process_stones(stone, stone_dict, stone_count, blinks)
    elif len(stone) % 2 == 0:
        first_stone = stone[:len(stone)//2]
        second_stone = str(int(stone[len(stone)//2:]))
        stone_dict, stone_count = process_stones(first_stone, stone_dict, stone_count, blinks)
        stone_dict, stone_count = process_stones(second_stone, stone_dict, stone_count, blinks)
    else:
        stone = str(int(stone) * 2024)
        stone_dict, stone_count = process_stones(stone, stone_dict, stone_count, blinks)
    stone_dict[(stone, blinks)] = [1, stone_count]
    return stone_dict, stone_count

# def solution_one():
#     stones = read_file()
#     blinks = 0
#     stone_dict = {}

#     while blinks < 25:
#         added_stones = []
#         for i in range(len(stones)):
#             new_stone, added_stone = process_stone(stones[i], stone_dict)
#             stones[i] = new_stone
#             if added_stone:
#                 added_stones.append(added_stone)
#         stones += added_stones
#         blinks += 1
#     return len(stones)
def solution_one():
    stones = read_file()
    stone_dict = {}
    count = 0
    for stone in stones:
        stone_dict, count = process_stones(stone, stone_dict, 0, 2)
    total = 0
    for key, value in stone_dict.items():
        total += (int(value[0]) * int(value[1]))
    return total

def solution_two():
    return
    stones = read_file()
    stone_dict = {}
    count = 0
    for stone in stones:
        stone_dict, count = process_stones(stone, stone_dict, 0, 75)
    total = 0
    for key, value in stone_dict.items():
        total += (int(value[0]) * int(value[2]))
    return total

if __name__ == '__main__':
    answer_one = solution_one() #239714
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
