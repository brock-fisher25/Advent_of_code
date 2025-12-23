def read_file():
    file = open("input.txt", "r")
    return file

def solution_one():
    file = read_file()
    dial = 50
    zeroes = 0
    for instruction in file:
        direction = instruction[0]
        clicks = int(instruction[1:])
        if direction == 'L':
            dial = dial - clicks
        else:
            dial = dial + clicks
        if dial % 100 == 0:
            zeroes = zeroes + 1
    return zeroes
        
# def solution_two():
#     file = read_file()
#     dial = 50
#     zeroes = 0
#     double_up = False
#     for instruction in file:
#         direction = instruction[0]
#         clicks = int(instruction[1:])
#         dial_bot = int(dial/100) * 100
#         if dial < 0:
#             dial_top = (int(dial/100) - 1) * 100
#         else:
#             dial_top = (int(dial/100) + 1) * 100
#         if direction == 'L':
#             if dial - clicks < dial_bot:
#                 zeroes = zeroes + 1
#                 double_up = True
#             dial = dial - clicks
#         else:
#             if dial + clicks > dial_top:
#                 zeroes = zeroes + 1
#                 double_up = True
#             dial = dial + clicks
#         if clicks > 99:
#             zeroes = zeroes + int(clicks/100)
#             if double_up:
#                 zeroes = zeroes - 1
#         double_up = False
#     return zeroes

def solution_two():
    file = read_file()
    dial = 50
    zeroes = 0
    for instruction in file:
        direction = instruction[0]
        clicks = int(instruction[1:])
        for i in range(clicks):
            if direction == 'L':
                dial = dial - 1
                if dial < 0:
                    dial = 99
            else:
                dial = dial + 1
                if dial > 99:
                    dial = 0
            if dial == 0:
                zeroes = zeroes + 1

    return zeroes

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)

