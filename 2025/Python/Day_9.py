import shapely
from shapely import Polygon

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
    for line in file:
        line = line.strip()
        tmp = line.split(',')
        new_coord = [int(tmp[1]), int(tmp[0])]
        coordinates.append(new_coord)
    polygon = Polygon(coordinates)
    # check all rectangles for max area
    area = 0
    for i in range(len(coordinates)):
        coord1 = coordinates[i]
        for j in range(i+1, len(coordinates)):
            coord2 = coordinates[j]
            new_coords = [coord1, [coord1[0], coord2[1]], coord2, [coord2[0], coord1[1]]]
            new_poly = Polygon(new_coords)
            if polygon.contains(new_poly):
                new_area = calculate_area(coord1, coord2)
                if area < new_area:
                    area = new_area
    return area

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two) # 3055280990 is too high
