def read_text_file():
    with open('Day_1_input.txt') as file:
        return file.readline()

def first_part():
    data = read_text_file()
    final_floor = 0
    for i in data:
        if i == '(':
            final_floor += 1
        else:
            final_floor -= 1
    return final_floor

    

def second_part():
    data = read_text_file()
    final_floor = 0
    for i in range(len(data)):
        if data[i] == '(':
            final_floor += 1
        else:
            final_floor -= 1
        if final_floor < 0:
            return i + 1
    return "Basement never reached"



if __name__ == "__main__":
    print(first_part()) #returns 138
    print(second_part()) #returns 1771
