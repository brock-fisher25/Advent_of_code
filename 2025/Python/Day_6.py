def read_file():
    file = open('input.txt', 'r')
    return file

def solution_one():
    file = read_file()
    sum = 0
    nums = []
    operators = []
    all_ops = ['*','-','+','/']
    for line in file:
        line = line.strip()
        temp = line.split(' ')
        if temp[0] in all_ops:
            for tmp in temp:
                if tmp == '':
                    continue
                operators.append(tmp)
        else:
            for tmp in temp:
                if tmp == '':
                    continue
                nums.append(tmp)
    num_columns = len(operators)
    grouped_equations = []
    for i in range(num_columns):
        new_equation = []
        for j in range(i, len(nums), num_columns):
            new_equation.append(nums[j])
        grouped_equations.append(new_equation)
    for i in range(num_columns):
        total = 0
        if operators[i] == '*':
            for num in grouped_equations[i]:
                if total == 0:
                    total = int(num)
                    continue
                total = total * int(num)
        elif operators[i] == '+':
            for num in grouped_equations[i]:
                total = total + int(num)
        sum += total
    return sum

def solution_two():
    file = read_file()
    sum = 0
    nums_map = []
    operators = []
    all_ops = ['*','+']
    for line in file:
        if line[0] in all_ops:
            for tmp in line:
                if tmp == '' or tmp == ' ' or tmp == '\n':
                    continue
                operators.append(tmp)
        else:
            nums_map.append(list(line[:len(line)-1]))
    equation_len = len(nums_map[0])
    col_indexes = []
    for i in range(equation_len):
        if nums_map[0][i] == ' ':
            is_col = True
            for j in range(len(nums_map)):
                if nums_map[j][i] != ' ':
                    is_col = False
                    break
            if is_col:
                col_indexes.append(i)
    col_indexes.append(equation_len)
    for index in col_indexes:
        nums = []
        prev_index = -1
        for i in range(index-1, prev_index, -1):
            num = ''
            for j in range(len(nums_map)):
                if nums_map[j][i] == ' ':
                    continue
                num += nums_map[j][i]
            nums.append(num)
    operators = operators[::-1]
    grouped_equations = []
    new_equation = []
    for i in range(len(nums)):
        if nums[i] == '':
            grouped_equations.append(new_equation)
            new_equation = []
            continue
        new_equation.append(nums[i])
    grouped_equations.append(new_equation)
    # do the math
    for i in range(len(operators)):
        total = 0
        if operators[i] == '*':
            for num in grouped_equations[i]:
                if total == 0:
                    total = int(num)
                    continue
                total = total * int(num)
        elif operators[i] == '+':
            for num in grouped_equations[i]:
                total = total + int(num)
        sum += total
    return sum



if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)