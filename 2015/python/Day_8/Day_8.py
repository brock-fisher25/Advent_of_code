
def read_text_file():
    with open('Day_8_input.txt') as file:
        return file.readlines()

def manipulate_string(string):
    #string = string.replace('\\\\', '\\')
  #  string = string.replace('\"', '"')
    count_slashes = string.count('\\\\')
    count_single_quotes = string.count('\\"')
    count_x = string.count('\\x')
    print("start")
    print(count_x)
    print(count_slashes)
    print(count_single_quotes)
    print("end")
    return (count_x * 3) + count_slashes + count_single_quotes
    


def first_part():
    list_of_strings = read_text_file()
    num_chars_literal = 0
    count = 0
    num_chars_mem = 0
    for string in list_of_strings:
        s1 = string.strip()
        print(s1)
        num_chars_literal += (len(s1))
        s2 = s1[1:-1]
        subtract = manipulate_string(s2)
        num_chars_mem += (len(s2) - subtract)
        print(subtract)
        print(len(s1))
        print(len(s2))
        print(num_chars_literal)
        print(num_chars_mem)
  #      count += 1
   #     if count == 5:
    #        exit()
    return num_chars_literal - num_chars_mem

def second_part():
    return

if __name__ == "__main__":
    print(first_part()) #returns 1362 is too high
    print(second_part()) #returns