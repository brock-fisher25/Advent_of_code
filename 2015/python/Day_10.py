def read_file():
    file = open('input.txt', 'r')
    return file

def solution_two():
    file = read_file()
    input = ''
    iterations = 50
    for line in file:
        input = line.strip()
    counter = 0
    while counter < iterations:
        current_digit = input[0]
        new_str = ''
        i = 0
        while i < len(input):
            digit_counter = 0
            all_same = True
            for j in range(i, len(input)):
                if input[i] == input[j] and j <= len(input) - 1:
                    digit_counter += 1
                    continue
                else:
                    all_same = False
                    i = j
                    break
            new_str += str(digit_counter)
            new_str += current_digit
            current_digit = input[i]
            if all_same:
                break

        input = new_str
        counter += 1

    return len(input)

def solution_one():
    file = read_file()
    input = ''
    iterations = 40
    for line in file:
        input = line.strip()
    counter = 0
    while counter < iterations:
        current_digit = input[0]
        new_str = ''
        i = 0
        while i < len(input):
            digit_counter = 0
            all_same = True
            for j in range(i, len(input)):
                if input[i] == input[j] and j <= len(input) - 1:
                    digit_counter += 1
                    continue
                else:
                    all_same = False
                    i = j
                    break
            new_str += str(digit_counter)
            new_str += current_digit
            current_digit = input[i]
            if all_same:
                break

        input = new_str
        counter += 1

    return len(input)

if __name__ == '__main__':
    print(solution_one())
    print(solution_two())
