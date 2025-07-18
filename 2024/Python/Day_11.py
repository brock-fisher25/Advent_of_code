def read_file():
    file = open("input_day_11.txt", "r")
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

def process_stones(stone, stone_dict, stone_count, blinks):
    original_stone = stone
    if (stone, blinks) in stone_dict:
        return stone_dict[(stone, blinks)]
    if blinks == 0:
        return 1
    
    if stone == '0':
        stone = '1'
        stone_count = process_stones(stone, stone_dict, stone_count, blinks - 1)
    elif len(stone) % 2 == 0:
        first_stone = stone[:len(stone)//2]
        second_stone = str(int(stone[len(stone)//2:]))
        stone_count = process_stones(first_stone, stone_dict, stone_count, blinks - 1) + process_stones(second_stone, stone_dict, stone_count, blinks - 1)
    else:
        stone = str(int(stone) * 2024)
        stone_count = process_stones(stone, stone_dict, stone_count, blinks - 1)
    stone_dict[(original_stone, blinks)] = stone_count
    return stone_count

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
    blinks = 25
    for stone in stones:
        process_stones(stone, stone_dict, 0, blinks)
    total = 0
    for stone in stones:
        total += int(stone_dict[stone, blinks])
    return total

def solution_two():
    stones = read_file()
    stone_dict = {}
    blinks = 75
    for stone in stones:
        process_stones(stone, stone_dict, 0, blinks)
    total = 0
    for stone in stones:
        total += int(stone_dict[stone, blinks])
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
