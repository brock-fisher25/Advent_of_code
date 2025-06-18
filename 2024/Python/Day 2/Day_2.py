def read_file():
    file = open("C:\Documents\Personal\Github\Advent-of-code\input.txt", 'r')
    return file

def abs_difference(x, y):
    if abs(x - y) < 1 or abs(x - y) > 3:
        return False
    return True

def check_report(list):
    for i in range(1, len(list)):
        if abs_difference(list[i], list[i-1]) is False:
            return False
    return True

def solution_one():
    file = read_file()
    total = 0
    for line in file:
        temp = list(map(int, line.split(' ')))
        asc_temp = sorted(temp)
        desc_temp = sorted(temp, reverse=True)
        if temp == asc_temp or temp == desc_temp:
            if check_report(temp):
                total += 1
    return total

def solution_two():
    file = read_file()
    total = 0
    for line in file:
        temp = list(map(int, line.split(' ')))
        

    return total
    
if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
