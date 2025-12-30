def read_file():
    file = open('input.txt', 'r')
    return file

def increment_pwd(input):
    s = list(input)
    i = len(input) - 1
    while i >= 0:
        if s[i] == 'z':
            s[i] = 'a'
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    input = ''.join(s)
    return input

def find_next_pwd(input):
    password = ''
    while (True):
        first_rule = False
        second_rule = False
        third_rule = False
        # check first rule
        for i in range(len(input) - 2):
            char_value = ord(input[i])
            if char_value + 1 == ord(input[i+1]) and char_value + 2 == ord(input[i+2]):
                first_rule = True
                break
        # check 2nd rule
        if ('i' not in input and 'o' not in input and 'l' not in input):
            second_rule = True
        # check 3rd rule
        count_pairs = 0
        paired_letters = []
        for i in range(len(input) - 1):
            if input[i] == input[i+1] and input[i] not in paired_letters:
                count_pairs += 1
                paired_letters.append(input[i])
        if count_pairs > 1:
            third_rule = True
        # check if all rules passed
        if first_rule and second_rule and third_rule:
            password = input
            break
        # if not, increment string
        else:
            input = increment_pwd(input)
    return password

def solution_two():
    input = solution_one()
    # increment input 1 time
    incr_input = increment_pwd(input)
    return find_next_pwd(incr_input)

def solution_one():
    file = read_file()
    for line in file:
        input = line.strip()
    return find_next_pwd(input)

if __name__ == '__main__':
    print(solution_one())
    print(solution_two())
