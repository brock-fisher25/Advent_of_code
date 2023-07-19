
def read_text_file():
    with open('Day_8_input.txt') as file:
        return file.readlines()

def first_part():
    list_of_strings = read_text_file()
    num_chars_literal = 0
    num_chars_mem = 0
    for string in list_of_strings:
        s1 = string.strip() # get rid of \n char
        num_chars_literal += (len(s1))
        num_chars_mem += len(eval(s1))
    return num_chars_literal - num_chars_mem

def second_part():
    list_of_strings = read_text_file()

    sum = 0
    for string in list_of_strings:
        sum += 2 + string.count('\\') + string.count('"')

    return sum

if __name__ == "__main__":
    print(first_part()) #returns 1350
    print(second_part()) #returns 2085