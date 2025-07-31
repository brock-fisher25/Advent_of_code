def read_file():
    file = open("input.txt", "r")
    return file

def process_quadrant(matrix, beg_row, end_row, beg_col, end_col):
    quadrant_sum = 0
    for i in range(beg_row, end_row, 1):
        for j in range(beg_col, end_col, 1):
            quadrant_sum += matrix[i][j]
    return quadrant_sum

def process_robot(matrix, position, vector, rows, cols, seconds):
    x = position[1]
    y = position[0]
    for i in range(seconds):
        x += vector[1]
        y += vector[0]
        if x > rows - 1:
            x -= rows
        elif x < 0:
            x += rows
        if y > cols - 1:
            y -= cols
        elif y < 0:
            y += cols
    matrix[x][y] += 1
    return matrix

def solution_one():
    file = read_file()
    rows = 7
    cols = 11
    seconds = 100
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for line in file:
        # get position
        position = []
        temp = line.split('p=')
        temp2 = temp[1].split(' ')[0].split(',')
        position.append(int(temp2[0]))
        position.append(int(temp2[1]))
        # get vector
        vector = []
        temp = line.split('v=')
        temp2 = temp[1].split(',')
        vector.append(int(temp2[0]))
        vector.append(int(temp2[1]))
        matrix = process_robot(matrix, position, vector, rows, cols, seconds)
    mid_col = int(cols/2)
    mid_row = int(rows/2)
    tl_quadrant = process_quadrant(matrix, 0, mid_row, 0, mid_col)
    tr_quadrant = process_quadrant(matrix, 0, mid_row, mid_col + 1, cols)
    bl_quadrant = process_quadrant(matrix, mid_row + 1, rows, 0, mid_col)
    br_quadrant = process_quadrant(matrix, mid_row + 1, rows, mid_col + 1, mid_col)
    for i in matrix:
        print(i)
    return tl_quadrant + tr_quadrant + bl_quadrant + br_quadrant
def solution_two():
    total= 0
    return total

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
