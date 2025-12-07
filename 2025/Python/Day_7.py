visited = {}

def read_file():
    file = open('input.txt', 'r')
    return file

def find_timelines(map, i, j):
    if i == len(map) - 1:
        return 1
    if (i,j) in visited:
        return visited[i,j]
    if map[i][j] == '^':
        left = find_timelines(map, i, j-1)
        right = find_timelines(map, i, j+1)
        visited[i,j] = left + right
        return left + right
    return find_timelines(map, i+1, j)

def solution_one():
    file = read_file()
    sum = 0
    map = []
    for line in file:
        line = line.strip()
        map.append(list(line))
    for i in range(1, len(map)):
        for j in range(len(map[0])):
            if map[i-1][j] == 'S':
                map[i][j] = '|'
            elif map[i][j] == '^' and map[i-1][j] == '|':
                sum += 1
                map[i][j-1] = '|'
                map[i][j+1] = '|'
            elif map[i-1][j] == '|':
                map[i][j] = '|'

    return sum

def solution_two():
    file = read_file()
    sum = 0
    map = []
    for line in file:
        line = line.strip()
        map.append(list(line))
    starting_index = 0
    for i in range(len(map[0])):
        if map[0][i] == 'S':
            starting_index = i
            break
    sum = find_timelines(map, 1, starting_index)
    return sum



if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)