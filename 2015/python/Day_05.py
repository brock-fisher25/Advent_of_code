def read_text_file():
    with open('Day_5_input.txt') as file:
        return file.readlines()
    
def check_bad(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return True
    return False

def initiate_vowels():
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    return vowels

def check_good(s):
    vowels = initiate_vowels()
    prev_letter = ''
    two_in_row = False
# count # of vowels in string & letters appearing twice in a row
    for i in s:
        if i in vowels.keys():
            vowels[i] += 1
        if prev_letter == i:
            two_in_row = True
        prev_letter = i
    if two_in_row and sum(vowels.values()) > 2:
        return True
    return False
    
def first_part():
    data = read_text_file()
    nice_strings = 0
    for i in data:
        if check_bad(i) == False and check_good(i) == True:
            nice_strings += 1
    return nice_strings

def check_strings(substring_dict):
    has_pairs = False
    has_repeats = False
    for key in substring_dict:
        if substring_dict[key] > 1 and len(key) == 2:
            if key.count(key[0]) == len(key):
                triple = key + key[0]
                if triple not in substring_dict.keys():
                    has_pairs = True
                quad = triple + key[0]
                if quad in substring_dict.keys():
                    has_pairs = True
            else:
                has_pairs = True
        if len(key) == 3:
            if key[0] == key[2]:
                has_repeats = True
        if has_repeats and has_pairs:
            return has_repeats and has_pairs
    return False

def second_part():
    data = read_text_file()
    nice_strings = 0
    counter = 0
    for string in data:
        substring_dict = {}
        for i in range(len(string)):
            for j in range(i+2, len(string) + 1):
                substring = string[i:j]
                if substring in substring_dict:
                    substring_dict[substring] += 1
                else:
                    substring_dict[substring] = 1
                if j > i + 3:
                    break
        if check_strings(substring_dict):
            nice_strings += 1
    return nice_strings

if __name__ == "__main__":
    print(first_part()) #returns 238
    print(second_part()) #returns 69
