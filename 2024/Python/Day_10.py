def read_file():
    file = open("input.txt", "r")
    map = []
    for line in file:
        map.append(list(line.strip()))
    int_map = []
    for i in map:
        int_map.append([int(c) for c in i])
    return int_map

def check_vertical_edges(i, map):
    if i < 0 or i > len(map) -1:
        return False
    return True

def check_horiz_edges(i, j, map):
    if j < 0 or j > len(map[i]) - 1:
        return False
    return True

def recursive_one(i, j, map, total, value, visited):
    # base case 
    if map[i][j] == 9 and visited[i][j] == 0:
            visited[i][j] = 1
            return total + 1, visited
    # check up
    if check_vertical_edges(i-1, map):
        if value + 1 == map[i-1][j]:
            total, visited = recursive_one(i-1, j, map, total, value + 1, visited)
    # check right
    if check_horiz_edges(i, j+1, map):
        if value + 1 == map[i][j+1]:
            total, visited = recursive_one(i, j+1, map, total, value + 1, visited)
    # check down
    if check_vertical_edges(i+1, map):
        if value + 1 == map[i+1][j]:
            total, visited = recursive_one(i+1, j, map, total, value + 1, visited)
    # check left
    if check_horiz_edges(i, j-1, map):
        if value + 1 == map[i][j-1]:
            total, visited = recursive_one(i, j-1, map, total, value + 1, visited)

    return total, visited

def recursive_two(i, j, map, total, value):
    # base case 
    if map[i][j] == 9:
        return total + 1
    # check up
    if check_vertical_edges(i-1, map):
        if value + 1 == map[i-1][j]:
            total = recursive_two(i-1, j, map, total, value + 1)
    # check right
    if check_horiz_edges(i, j+1, map):
        if value + 1 == map[i][j+1]:
            total = recursive_two(i, j+1, map, total, value + 1)
    # check down
    if check_vertical_edges(i+1, map):
        if value + 1 == map[i+1][j]:
            total = recursive_two(i+1, j, map, total, value + 1)
    # check left
    if check_horiz_edges(i, j-1, map):
        if value + 1 == map[i][j-1]:
            total = recursive_two(i, j-1, map, total, value + 1)

    return total
    
def solution_one():
    map = read_file()
    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                visited = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
                score = 0
                score, visited = recursive_one(i, j, map, score, map[i][j], visited)
                total += score

    return total

def solution_two():
    map = read_file()
    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                score = 0
                score = recursive_two(i, j, map, score, map[i][j])
                total += score
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
