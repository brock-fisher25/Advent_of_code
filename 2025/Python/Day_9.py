def read_file():
    file = open('input.txt', 'r')
    return file

def calculate_area(coord1, coord2):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    length = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return length * height

def solution_one():
    file = read_file()
    area = 0
    coordinates = []
    for line in file:
        line = line.strip()
        tmp = line.split(',')
        coordinates.append([int(tmp[1]), int(tmp[0])])
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            new_area = calculate_area(coordinates[i], coordinates[j])
            if area < new_area:
                area = new_area
    return area

def solution_two():
    file = read_file()
    area = 0
    coordinates = []
    valid_row_ranges = {}
    valid_col_ranges = {}
    for line in file:
        line = line.strip()
        tmp = line.split(',')
        new_coord = [int(tmp[1]), int(tmp[0])]
        coordinates.append(new_coord)
    col_last = False
    for i in range(len(coordinates)):
        new_coord = coordinates[i]
        for j in range(i+1, len(coordinates)):
            next_coord = coordinates[j]
            # if rows don't match, columns must match
            if new_coord[0] != next_coord[0]:
                col_last = True
                higher = max(new_coord[0], next_coord[0])
                lower = min(new_coord[0], next_coord[0])
                new_range = [lower, higher]
                if new_coord[1] not in valid_col_ranges.keys():
                    valid_col_ranges[new_coord[1]] = [new_range]
                else:
                    if new_range not in valid_col_ranges[new_coord[1]]:
                        valid_col_ranges[new_coord[1]].append(new_range)
            # else rows must match
            else:
                col_last = False
                higher = max(new_coord[1], next_coord[1])
                lower = min(new_coord[1], next_coord[1])
                new_range = [lower, higher]
                if new_coord[0] not in valid_row_ranges.keys():
                    valid_row_ranges[new_coord[0]] = [new_range]
                else:
                    if new_range not in valid_col_ranges[new_coord[0]]:
                        valid_row_ranges[new_coord[0]].append(new_range)
            break
    if not col_last:
        coord1 = coordinates[0]
        coord2 = coordinates[-1]
        higher = max(coord1[0], coord2[0])
        lower = min(coord1[0], coord2[0])
        new_range = [lower, higher]
        if coord1[1] not in valid_col_ranges.keys():
            valid_col_ranges[coord1[1]] = [new_range]
        else:
            if new_range not in valid_col_ranges[coord1[1]]:
                valid_col_ranges[coord1[1]].append(new_range)
    else:
        coord1 = coordinates[0]
        coord2 = coordinates[-1]
        higher = max(coord1[1], coord2[1])
        lower = min(coord1[1], coord2[1])
        new_range = [lower, higher]
        if coord1[0] not in valid_col_ranges.keys():
            valid_col_ranges[coord1[0]] = [new_range]
        else:
            if new_range not in valid_col_ranges[coord1[0]]:
                valid_col_ranges[coord1[0]].append(new_range)
    # check all rectangles for max area
    area = 0
    for i in range(len(coordinates)):
        coord1 = coordinates[i]
        for j in range(i+1, len(coordinates)):
            coord2 = coordinates[j]
            l_edge = True
            r_edge = True
            t_edge = True
            b_edge = True
            # check each edge of rectangle to ensure it is in shape
            # check to see if rectangle is a single horizontal line
            if coord1[0] == coord2[0]:
                t_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                b_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                l_edge = True
                r_edge = True
            # check to see if rectangle is a single vertical line
            elif coord1[1] == coord2[1]:
                l_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                r_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                b_edge = True
                t_edge = True
            else:
                t_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                b_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                l_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
                r_edge = check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2)
            if l_edge and r_edge and t_edge and b_edge:
                new_area = calculate_area(coord1, coord2)
                if area < new_area:
                    area = new_area
    return sum

def check_edge(valid_row_ranges, valid_col_ranges, coord1, coord2):
    return True



if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)