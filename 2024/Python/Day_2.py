def read_file():
    file = open("input.txt", 'r')
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

def final_check(list):
    asc_list = sorted(list)
    desc_list = sorted(list, reverse=True)
    if list == asc_list or list == desc_list:
        if check_report(list):
            return True
    return False

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
    incorrect_lists = []
    total = 0
    # create list of all reports in file that fail the first check (have at least 1 error wrong with them)
    for line in file:
        temp = list(map(int, line.split(' ')))
        asc_temp = sorted(temp)
        desc_temp = sorted(temp, reverse=True)
        if temp == asc_temp or temp == desc_temp:
            if check_report(temp):
                total += 1
            else:
                incorrect_lists.append(temp)
        else:
            incorrect_lists.append(temp)
    # now check and remove one element from the list at a time, then check the new list
    for curr_list in incorrect_lists:
        new_list = []
        for j in range (0, len(curr_list)):
            if final_check(curr_list[:j]+curr_list[j+1:]):
                total += 1
                break
    return total
    
if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
