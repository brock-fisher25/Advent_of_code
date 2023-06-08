# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?
#
# Your puzzle answer was 238.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# 
# Now, a nice string is one with all of the following properties:
# 
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:
#
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?
# ----------------------------------------------------------------------------

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
        if substring_dict[key] > 2 and len(key) > 1:
            has_pairs = True
        if len(key) == 3:
            if key[0] == key[2]:
                has_repeats = True
    return has_repeats and has_pairs





def second_part():
    data = read_text_file()
    substring_dict = {}
    nice_strings = 0
    for string in data:
        for i in range(len(string)):
            for j in range(i+1, len(string) + 1):
                substring = string[i:j]
                if substring in substring_dict:
                    substring_dict[substring] += 1
                else:
                    substring_dict[substring] = 1
        if check_strings(substring_dict):
            nice_strings += 1
    return

if __name__ == "__main__":
    print(first_part()) #returns 238
    print(second_part()) #returns 2341
