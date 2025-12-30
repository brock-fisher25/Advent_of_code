def read_text_file():
    with open('Day_2_input.txt') as file:
        return file.readlines()

def first_part():
    data = read_text_file()
    total_sqft = 0
    for i in data:
        lwh = i.split('x')
        lwh = [eval(i) for i in lwh]
        lwh.sort()
        slack = lwh[0] * lwh[1]
        first_side = lwh[0] * lwh[1]
        second_side = lwh[1] * lwh[2]
        third_side = lwh[0] * lwh[2]
        total_area = 2*(first_side + second_side + third_side)
        total_sqft += slack + total_area
    return total_sqft

def second_part():
    data = read_text_file()
    total_ribbon = 0
    for i in data:
        lwh = i.split('x')
        lwh = [eval(i) for i in lwh]
        lwh.sort()
        perimeter = 2 * (lwh[0] + lwh[1])
        volume = lwh[0] * lwh[1] * lwh[2]
        total_ribbon += perimeter + volume
    return total_ribbon

if __name__ == "__main__":
    print(first_part()) #returns 1606483
    print(second_part()) #returns 3842356
