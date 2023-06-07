# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
#
# For example:
#
# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
# Your puzzle answer was 2081.
#
# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
# 
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
# Your puzzle answer was 2341.
# 
# Both parts of this puzzle are complete! They provide two gold stars: **
# ----------------------------------------------------------------------------

def read_text_file():
    with open('data.txt') as file:
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
    

def second_part():
    data = read_text_file()
    substring_dict = {}
    for i in range(len(data)):
        for j in range(i+1, len(data) + 1):
            substring = data[i:j]
            if substring in substring_dict:
                substring_dict[substring] += 1
            else:
                substring_dict[substring] = 1
    print(substring_dict)
    return

if __name__ == "__main__":
    print(first_part()) #returns 238
    print(second_part()) #returns 2341
