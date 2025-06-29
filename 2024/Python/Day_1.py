def read_file():
    file = open("input.txt", 'r')
    return file

def solution_one():
    file = read_file()
    list_1 = []
    list_2 = []
    for line in file:
        temp = line.split('   ')
        list_1.append(int(temp[0]))
        list_2.append(int(temp[1]))
    
    list_1.sort()
    list_2.sort()
    total = 0
    for i in range(len(list_1)):
        total += abs(list_2[i] - list_1[i])
    return total

def solution_two():
    file = read_file()
    dict_1 = {}
    list_2 = []
    for line in file:
        temp = line.split('   ')
        dict_1[int(temp[0])] = 0
        list_2.append(int(temp[1]))

    for i in list_2:
        if i not in dict_1.keys():
            continue
        dict_1[i] += 1
    
    total = 0

    for key, value in dict_1.items():
        total += (key * value)

    return total
    
    


if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()

    print(answer_one)
    print(answer_two)
