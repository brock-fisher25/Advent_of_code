def read_file():
    file = open('input.txt', 'r')
    return file

def process_input(input):
    sum = 0
    temp = input.split('-')
    first = int(temp[0])
    last = int(temp[1])
    for i in range(first, last+1):
        num_string = str(i)
        if len(num_string) == 1:
            continue
        if len(num_string) % 2 != 0:
            continue
        middle = int(len(num_string)/2)
        first = num_string[:middle]
        last = num_string[middle:]
        if first == last:
            sum = sum + i
    return sum

def solution_one():
    file = read_file()
    for line in file:
        inputs = line.split(',')
    sum = 0
    for input in inputs:
        sum = sum + process_input(input)
    return sum
    
def solution_two():
    file = read_file()
    for line in file:
        inputs = line.split(',')
    sum = 0
    for input in inputs:
        temp = input.split('-')
        first = int(temp[0])
        last = int(temp[1])
        for i in range(first, last+1):
            num_string = str(i)
            if len(num_string) == 1:
                continue
            middle = int(len(num_string)/2)
            substrings = []
            substring = ''
            for j in range(middle):
                substring = substring + num_string[j]
                substrings.append(substring)
            for substr in substrings:
                parts = []
                for k in range(0, len(num_string), len(substr)):
                    parts.append(num_string[k:k + len(substr)])
                if len(set(parts)) == 1:
                    sum = sum + i
                    break
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    answer_two = solution_two()
    print(answer_one)
    print(answer_two)
