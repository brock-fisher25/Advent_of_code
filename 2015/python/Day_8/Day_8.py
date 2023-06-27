
def read_text_file():
    with open('Day_8_input.txt') as file:
        return file.readlines()

def manipulate_string(string):
    string = string.replace('\\\\', '\\')
    string = string.replace('\"', '"')
    print(string)
    return string
    


def first_part():
    list_of_strings = read_text_file()
    num_chars_literal = 0
    count = 0
    num_chars_mem = 0
    for string in list_of_strings:
        s1 = string.strip() # get rid of \n char
        num_chars_literal += (len(s1))
        print(s1)
        mem_string = manipulate_string(s1)
        num_chars_mem += (len(s1) - len(mem_string))
        if count == 5:
            exit()
        count += 1
    return num_chars_literal - num_chars_mem

def second_part():
    return

if __name__ == "__main__":
    print(first_part()) #returns 1362 is too high
    print(second_part()) #returns