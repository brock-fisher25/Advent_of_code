import hashlib

def first_part():
    base_input = 'ckczppom'
    input = base_input 
    lowest_num = 1
    while True:
        input += str(lowest_num)
        encoded = input.encode()
        result = hashlib.md5(encoded)
        if result.hexdigest().startswith('00000'):
            return lowest_num
        lowest_num += 1
        input = base_input

def second_part():
    base_input = 'ckczppom'
    input = base_input 
    lowest_num = 1
    while True:
        input += str(lowest_num)
        encoded = input.encode()
        result = hashlib.md5(encoded)
        if result.hexdigest().startswith('000000'):
            return lowest_num
        lowest_num += 1
        input = base_input

if __name__ == "__main__":
    print(first_part()) #returns 117946
    print(second_part()) #returns 3938038
