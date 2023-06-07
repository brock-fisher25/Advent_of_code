# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
#
# For example:
#
# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
# Your puzzle answer was 2081.
#
# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
# 
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
# Your puzzle answer was 2341.
# 
# Both parts of this puzzle are complete! They provide two gold stars: **
# ----------------------------------------------------------------------------


def read_text_file():
    with open('Day_3_input.txt') as file:
        return file.readline()

def first_part():
    data = read_text_file()
    up, down, left, right = 0, 0, 0, 0
    for i in data:
        if i == '<':
            left += 1
        elif i == '>':
            right += 1
        elif i == '^':
            up += 1
        else:
            down += 1
    vert = max(up, down)
    horiz = max(left, right)
    map = [[0 for i in range(int(vert))] for j in range(int(horiz))]
    horiz_position = int(horiz/2)
    vert_position = int(vert/2)
    map[vert_position][horiz_position] = 1
    for i in data:
        map[vert_position][horiz_position] += 1
        if i == '<':
            horiz_position -= 1
        elif i =='>':
            horiz_position += 1
        elif i =='^':
            vert_position -= 1
        else: 
            vert_position += 1
    unique_houses = 0
    for i in map:
        for j in i:
            if j > 0:
                unique_houses += 1
    return unique_houses

def second_part():
    data = read_text_file()
    up, down, left, right = 0, 0, 0, 0
    for i in data:
        if i == '<':
            left += 1
        elif i == '>':
            right += 1
        elif i == '^':
            up += 1
        else:
            down += 1
    vert = up + down
    horiz = left + right
    map = [[0 for i in range(int(vert))] for j in range(int(horiz))]
    santa_horiz_position = int(horiz/2)
    santa_vert_position = int(vert/2)
    robot_horiz_position = int(horiz/2)
    robot_vert_position = int(vert/2)
    map[santa_vert_position][santa_horiz_position] = 1
    i = 0 # santa counter
    j = 1 # robot counter
    while i < len(data) - 2:
        map[santa_vert_position][santa_horiz_position] += 1
        if data[i] == '<':
            santa_horiz_position -= 1
        elif data[i] =='>':
            santa_horiz_position += 1
        elif data[i] =='^':
            santa_vert_position -= 1
        else: 
            santa_vert_position += 1
        map[robot_vert_position][robot_horiz_position] += 1
        if data[j] == '<':
            robot_horiz_position -= 1
        elif data[j] =='>':
            robot_horiz_position += 1
        elif data[j] =='^':
            robot_vert_position -= 1
        else: 
            robot_vert_position += 1
        i += 2
        j += 2
    unique_houses = 0
    for i in map:
        for j in i:
            if j > 0:
                unique_houses += 1
    return unique_houses

if __name__ == "__main__":
    print(first_part()) #returns 2081
    print(second_part()) #returns 2341
