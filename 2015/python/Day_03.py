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
