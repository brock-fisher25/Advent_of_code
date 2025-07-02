def read_file():
    file = open("input_day_7.txt", "r")
    return file

def check_node(node, result_map):
    if node[0] >= 0 and node[0] <= len(result_map) - 1 and node[1] >= 0 and node[1] <= len(result_map[0]) - 1:
        result_map[node[0]][node[1]] = '#'
        return result_map, False
    return result_map, True

def check_map_two(result_map, i, j, vert_index, hor_index):
    hor_distance = abs(j - hor_index)
    vert_distance = abs(i - vert_index)
    top_node_pos = [i, j]
    bot_node_pos = [vert_index, hor_index]
    forward_slash, back_slash, pipe = False, False, False
    back_slash = False
    # first node is to the right of second node
    if top_node_pos[1] > bot_node_pos[1]:
        forward_slash = True
    # first node is to the left of second node
    elif top_node_pos[1] < bot_node_pos[1]:
        back_slash = True
    else:
        # nodes are stacked
        pipe = True
    # loop through entire result map, turning entire lines into antinodes
    # build antinodes above
    done = False
    for _ in range(i,-1,-1):
        new_node = []
        i = i - vert_distance
        new_node.append(i)
        if forward_slash:
            j = j + hor_distance
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        elif back_slash:
            j = j - hor_distance
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        elif pipe:
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        if done:
            break
    # build antinodes below
    done = False
    for _ in range(i, len(result_map)):
        new_node = []
        i = i + vert_distance
        new_node.append(i)
        if forward_slash:
            j = j - hor_distance
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        elif back_slash:
            j = j + hor_distance
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        elif pipe:
            new_node.append(j)
            result_map, done = check_node(new_node, result_map)
        if done:
            break
    return result_map


def check_map(result_map, i, j, vert_index, hor_index):
    hor_distance = abs(j - hor_index)
    vert_distance = abs(i - vert_index)
    first_antinode = []
    second_antinode = []
    # handle all cases where the antinodes fall off the map
    # first antinode is always above the current char, second is always below
    first_antinode.append(i - vert_distance)
    second_antinode.append(vert_index + vert_distance)
    # second char is to the right of the first char
    if hor_index > j:
        first_antinode.append(j - hor_distance)
        second_antinode.append(hor_index + hor_distance)
    # second char is to the left of the first char
    elif hor_index < j:
        first_antinode.append(j + hor_distance)
        second_antinode.append(hor_index - hor_distance)
    # chars are stacked on top of one another
    else:
        first_antinode.append(j)
        second_antinode.append(j)
    # check to see if you process one or both nodes
    if first_antinode[0] >= 0 and first_antinode[1] >= 0 and first_antinode[1] <= len(result_map[0]) - 1 and first_antinode[0] <= len(result_map) - 1:
        result_map[first_antinode[0]][first_antinode[1]] = '#'
    if second_antinode[0] >= 0 and second_antinode[1] >= 0 and second_antinode[1] <= len(result_map[0]) - 1 and second_antinode[0] <= len(result_map) - 1:
        result_map[second_antinode[0]][second_antinode[1]] = '#'        
    return result_map


def create_result_map(result_map, char, orig_map, sol_one):
    for i in range(len(orig_map)):
        for j in range(len(orig_map[i])):
            if orig_map[i][j] == char:
                for vert_index in range(i+1, len(orig_map)):
                    for hor_index in range(len(orig_map[vert_index])):
                        if orig_map[vert_index][hor_index] == char:
                            if sol_one:
                                result_map = check_map(result_map, i, j, vert_index, hor_index)
                            else:
                                result_map = check_map_two(result_map, i, j, vert_index, hor_index)
    return result_map

def solution_one():
    file = read_file()
    chars = []
    orig_map = []
    total = 0
    # get list of all different characters possible throughout map, and create a blank map
    cols = 0
    rows = 0
    for line in file:
        char_array = list(line.strip())
        orig_map.append(char_array)
        cols = len(line)
        for char in line:
            if char not in chars and char != '.' and char != '\n':
                chars.append(char)
        rows += 1
    result_map = [['.'] * cols for _ in range(rows)]
    for char in chars:
        result_map = create_result_map(result_map, char, orig_map, True)
    for line in result_map:
        if '#' in line:
            total += line.count('#')
    return total

def solution_two():
    file = read_file()
    chars = []
    orig_map = []
    char_map = []
    total = 0
    # get list of all different characters possible throughout map, and create a blank map
    cols = 0
    rows = 0
    for line in file:
        char_array = list(line.strip())
        orig_map.append(char_array)
        cols = len(line)
        for char in line:
            if char not in chars and char != '.' and char != '\n':
                chars.append(char)
        rows += 1
    result_map = [['.'] * cols for _ in range(rows)]
    for char in chars:
        result_map = create_result_map(result_map, char, orig_map, False)
    for line in result_map:
        if '#' in line:
            total += line.count('#')
    return total




if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
