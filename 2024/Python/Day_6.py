import os

os.chdir("C:\Documents\Personal\Github\Advent-of-code")

def read_file():
    file = open("input.txt", "r")
    return file

def found_edge(map, y, x):
    if y == 0 or y == len(map)-1 or x == 0 or x == len(map[y]) - 1:
        return True
    return False

# check to see if path is clear
def check_path(position):
    if position == '#':
        return False
    return True

def not_visited(position):
    if position == '.':
        return True
    return False

def move_position_loop(map, y, x, map_tracker):
    edge_found = False
    loop_found = False
    y2, x2 = y, x
    if map[y][x] == '^':
        y2 -= 1
        if not found_edge(map, y, x):
            if check_path(map[y2][x]):
                map[y2][x] = '^'
                map[y][x] = 'X'
                y = y2
            else:
                if [y, x, '^'] in map_tracker:
                    loop_found = True
                else:
                    map_tracker.append([y, x, '^'])
                    map[y][x] = '>'
        else:
            edge_found = True
    elif map[y][x] == '>':
        x2 += 1
        if not found_edge(map, y, x):
            if check_path(map[y][x2]):
                map[y][x2] = '>'
                map[y][x] = 'X'
                x = x2
            else:
                if [y, x, '>'] in map_tracker:
                    loop_found = True
                else:
                    map_tracker.append([y, x, '>'])
                    map[y][x] = 'v'
        else:
            edge_found = True
    elif map[y][x] == 'v':
        y2 += 1
        if not found_edge(map, y, x):
            if check_path(map[y2][x]):
                map[y2][x] = 'v'
                map[y][x] = 'X'
                y = y2
            else:
                if [y, x, 'v'] in map_tracker:
                    loop_found = True
                else:
                    map_tracker.append([y, x, 'v'])
                    map[y][x] = '<'
        else:
            edge_found = True
    elif map[y][x] == '<':
        x2 -= 1
        if not found_edge(map, y, x):
            if check_path(map[y][x2]):
                map[y][x2] = '<'
                map[y][x] = 'X'
                x = x2
            else:
                if [y, x, '<'] in map_tracker:
                    loop_found = True
                else:
                    map_tracker.append([y, x, '<'])
                    map[y][x] = '^'
        else:
            edge_found = True
    return map, map_tracker, edge_found, loop_found, y, x

def move_position(map, y, x, total):
    y2, x2 = y, x
    edge_found = False
    if map[y][x] == '^':
        y2 -= 1
        if not found_edge(map, y, x):
            if check_path(map[y2][x]):
                if not_visited(map[y2][x]):
                    total += 1
                map[y2][x] = '^'
                map[y][x] = 'X'
                y = y2
            else:
                map[y][x] = '>'
        else:
            edge_found = True
    elif map[y][x] == '>':
        x2 += 1
        if not found_edge(map, y, x):
            if check_path(map[y][x2]):
                if not_visited(map[y][x2]):
                    total += 1
                map[y][x2] = '>'
                map[y][x] = 'X'
                x = x2
            else:
                map[y][x] = 'v'
        else:
            edge_found = True
    elif map[y][x] == 'v':
        y2 += 1
        if not found_edge(map, y, x):
            if check_path(map[y2][x]):
                if not_visited(map[y2][x]):
                    total += 1
                map[y2][x] = 'v'
                map[y][x] = 'X'
                y = y2
            else:
                map[y][x] = '<'
        else:
            edge_found = True
    elif map[y][x] == '<':
        x2 -= 1
        if not found_edge(map, y, x):
            if check_path(map[y][x2]):
                if not_visited(map[y][x2]):
                    total += 1
                map[y][x2] = '<'
                map[y][x] = 'X'
                x = x2
            else:
                map[y][x] = '^'
        else:
            edge_found = True
    return map, edge_found, total, y, x

def solution_one():
    file = read_file()
    temp = []
    map = []
    x, y = 0, 0
    markers = ['^','v','<','>']
    for line in file:
        temp.append(line.strip())
    for x in temp:
        map.append(list(x))

    for i in range(len(map)):
        for mark in markers:
            if mark in map[i]:
                for j in range(len(map[i])):
                    if map[i][j] in markers:
                        y = i
                        x = j
    total = 1
    while True:
        map, found_edge, total, y, x = move_position(map, y, x, total)
        if found_edge:
            break

    return total

def solution_two():
    file = read_file()
    temp = []
    map = []
    x, y = 0, 0
    markers = ['^','v','<','>']
    for line in file:
        temp.append(line.strip())
    for x in temp:
        map.append(list(x))
    for i in range(len(map)):
        for mark in markers:
            if mark in map[i]:
                for j in range(len(map[i])):
                    if map[i][j] in markers:
                        y = i
                        x = j
                        break
    total = 0
    y_orig, x_orig = y, x
    # replace one period at a time and then see if there is a loop
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#' or map[i][j] in markers:
                continue
            map[i][j] = '#'
            map_tracker = []
            while True:
                map, map_tracker, found_edge, found_loop, y, x = move_position_loop(map, y, x, map_tracker)
                if found_edge:
                    break
                if found_loop:
                    total += 1
                    break
            map[i][j] = '.'
            map[y][x] = '.'
            map[y_orig][x_orig] = '^'
            y, x = y_orig, x_orig
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
