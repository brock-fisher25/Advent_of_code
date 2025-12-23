def read_file():
    file = open('input.txt', 'r')
    return file

def solution_one():
    file = read_file()
    ranges = []
    ids = []
    sum = 0
    for line in file:
        if '-' in line:
            line = line.strip()
            temp = line.split('-')
            temp_range = [int(temp[0]), int(temp[1])]
            ranges.append(temp_range)
        elif line == '\n':
            continue
        else:
            line = line.strip()
            produce_id = int(line)
            ids.append(produce_id)
    for id in ids:
        for range in ranges:
            min = range[0]
            max = range[1]
            if id >= min and id <= max:
                sum += 1
                break
    return sum

def solution_two():
    file = read_file()
    sum = 0
    ranges = []
    for line in file:
        if '-' in line:
            line = line.strip()
            temp = line.split('-')
            range = [int(temp[0]), int(temp[1])]
            ranges.append(range)
    ranges = sorted(ranges, key=lambda x: x[0])
    print(ranges)
    prev_max = 0
    for range in ranges:
        print(range)
        if prev_max == 0:
            sum += (range[1] - range[0]) + 1
            prev_max = range[1]
            continue
        # check to see if current range min is greater than last ranges max
        if range[0] > prev_max:
            sum += (range[1] - range[0]) + 1
        elif range[1] < prev_max:
            continue
        # if not, then add from prev max to new max
        else:
            sum += (range[1] - prev_max)
        # update prev_max to new max
        prev_max = range[1]
    return sum



if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
