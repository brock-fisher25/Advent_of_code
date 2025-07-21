def read_file():
    file = open("input_day_12.txt", "r")
    map = []
    for line in file:
        map.append(list(line.strip()))
    return map

def calculate_perimeter(map, i, j):
    plant = map[i][j]
    count_left_side, count_right_side, count_top_side, count_bot_side = False, False, False, False
    if i == len(map) - 1:
        count_bot_side = True
    else:
        count_bot_side = map[i+1][j] != plant
    if i == 0:
        count_top_side = True
    else:
        count_top_side = map[i-1][j] != plant
    if j == len(map[0]) - 1:
        count_right_side = True
    else:
        count_right_side = map[i][j+1] != plant
    if j == 0:
        count_left_side = True
    else:
        count_left_side = map[i][j-1] != plant
    return count_bot_side + count_left_side + count_right_side + count_top_side

def calculate_outside_corners(map, i, j, plant):

    tlc_found, trc_found, brc_found, blc_found = False, False, False, False
    # top left corner
    if i == 0 and j == 0:
        tlc_found = True
    # top edge
    elif i == 0:
        tlc_found = map[i][j-1] != plant
    # left edge
    elif j == 0:
        tlc_found = map[i-1][j] != plant
    # everywhere else
    else:
        tlc_found = (map[i-1][j] != plant and map[i][j-1] != plant) or (map[i][j-1] == plant and map[i-1][j] == plant and map[i-1][j-1] != plant)

    # top right corner
    if i == 0 and j == len(map[0]) - 1:
        trc_found = True
    # top edge
    elif i == 0:
        trc_found = map[i][j+1] != plant
    # right edge
    elif j == len(map[0]) - 1:
        trc_found = map[i-1][j] != plant
    # everywhere else
    else:
        trc_found = (map[i-1][j] != plant and map[i][j+1] != plant) or (map[i-1][j] == plant and map [i][j+1] == plant and map[i-1][j+1] != plant)

    # bottom right corner
    if i == len(map) - 1 and j == len(map[0]) - 1:
        brc_found = True
    # bottom edge
    elif i == len(map) - 1:
        brc_found = map[i][j+1] != plant
    # right edge
    elif j == len(map[0]) - 1:
        brc_found = map[i+1][j] != plant
    # everywhere else
    else:
        brc_found = (map[i+1][j] != plant and map[i][j+1] != plant) or (map[i+1][j] == plant and map[i][j+1] == plant and map[i+1][j+1] != plant)

    # bottom left corner
    if i == len(map) - 1 and j == 0:
        blc_found = True
    # bottom edge
    elif i == len(map) - 1:
        blc_found = map[i][j-1] != plant
    # left edge
    elif j == 0:
        blc_found = map[i+1][j] != plant
    # everywhere else
    else:
        blc_found = (map[i+1][j] != plant and map[i][j-1] != plant) or (map[i+1][j] == plant and map[i][j-1] == plant and map[i+1][j-1] != plant)

    return tlc_found + trc_found + brc_found + blc_found



def calculate_plant(plant, perimeter, area, i, j, map, blank_map):
    if j > len(map[0]) - 1 or j < 0:
        return perimeter, area, blank_map
    if map[i][j] != plant or blank_map[i][j] == '0':
        return perimeter, area, blank_map
    area += 1
    perimeter += calculate_perimeter(map, i, j)
    blank_map[i][j] = '0'
    # go up
    if i > 0:
        perimeter, area, blank_map = calculate_plant(plant, perimeter, area, i-1, j, map, blank_map)
    # go right
    if j < len(map[0]) - 1:
        perimeter, area, blank_map = calculate_plant(plant, perimeter, area, i, j+1, map, blank_map)
    # go down
    if i < len(map) - 1:
        perimeter, area, blank_map = calculate_plant(plant, perimeter, area, i+1, j, map, blank_map)
    # go left
    if j > 0:
        perimeter, area, blank_map = calculate_plant(plant, perimeter, area, i, j-1, map, blank_map)
    return perimeter, area, blank_map

def calculate_plant_2(plant, sides, area, i, j, map, blank_map):
    if map[i][j] != plant or blank_map[i][j] == '0':
        return sides, area, blank_map
    area += 1
    sides += calculate_outside_corners(map, i, j, plant)
    blank_map[i][j] = '0'
    # go up
    if i > 0:
        sides, area, blank_map = calculate_plant_2(plant, sides, area, i-1, j, map, blank_map)
    # go right
    if j < len(map[0]) - 1:
        sides, area, blank_map = calculate_plant_2(plant, sides, area, i, j+1, map, blank_map)
    # go down
    if i < len(map) - 1:
        sides, area, blank_map = calculate_plant_2(plant, sides, area, i+1, j, map, blank_map)
    # go left
    if j > 0:
        sides, area, blank_map = calculate_plant_2(plant, sides, area, i, j-1, map, blank_map)
    return sides, area, blank_map


def solution_one():
    map = read_file()
    blank_map = [["." for _ in range(len(map))] for _ in range(len(map[0]))]
    plants = {}
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if blank_map[i][j]  == '.':
                perimeter = 0
                area = 0
                plant = map[i][j]
                perimeter, area, blank_map = calculate_plant(plant, perimeter, area, i, j, map, blank_map)
                plants[counter] = [0,0]
                plants[counter][0] = perimeter
                plants[counter][1] = area
                counter += 1
    total = 0
    for key, value in plants.items():
        total += (value[0] * value[1])
    return total

def solution_two():
    map = read_file()
    blank_map = [["." for _ in range(len(map))] for _ in range(len(map[0]))]
    plants = {}
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if blank_map[i][j]  == '.':
                perimeter = 0
                area = 0
                plant = map[i][j]
                perimeter, area, blank_map = calculate_plant_2(plant, perimeter, area, i, j, map, blank_map)
                plants[counter] = [0,0]
                plants[counter][0] = perimeter
                plants[counter][1] = area
                counter += 1
    total = 0
    for key, value in plants.items():
        total += (value[0] * value[1])
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
