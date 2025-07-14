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

def solution_one():
    stones = read_file()
    blinks = 0
    stone_dict = {}

    while blinks < 25:
        added_stones = []
        for i in range(len(stones)):
            new_stone, added_stone = process_stone(stones[i], stone_dict)
            stones[i] = new_stone
            if added_stone:
                added_stones.append(added_stone)
        stones += added_stones
        blinks += 1
    return len(stones)

def solution_two():
    stones = read_file()
    blinks = 0
    stone_dict = {}

    while blinks < 75:
        added_stones = []
        for i in range(len(stones)):
            new_stone, added_stone = process_stone(stones[i], stone_dict)
            stones[i] = new_stone
            if added_stone:
                added_stones.append(added_stone)
        stones += added_stones
        blinks += 1
    return len(stones)

if __name__ == '__main__':
    answer_one = solution_one() #239714
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
