def read_file():
    file = open('input.txt', 'r')
    return file

def solution_one():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
        if 'x' in line:
            tmp = line.split(':')
            tmp2 = tmp[0].split('x')
            length = int(tmp2[0])
            height = int(tmp2[1])
            index_count = [int(x) for x in tmp[1].strip().split(' ')]
            num_presents = 0
            for i in index_count:
                num_presents += i
            total_space = length * height
            total_needed_space = num_presents * 9
            if total_needed_space <= total_space:
                sum += 1     
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
