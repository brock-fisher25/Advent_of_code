visited1 = {}
visited2 = {}

def read_file():
    file = open('input.txt', 'r')
    return file

def dfs1(curr_device, end, devices):
    if end in devices[curr_device]:
        return 1
    if curr_device in visited1:
        return visited1[curr_device]
    sum = 0
    for device in devices[curr_device]:
        sum += dfs1(device, end, devices)
    visited1[curr_device] = sum
    return sum

def dfs2(curr_device, end, devices, seen_dac, seen_fft):
    if curr_device == 'dac':
        seen_dac = True
    if curr_device == 'fft':
        seen_fft = True

    if end in devices[curr_device]:
        return 1 if seen_fft and seen_dac else 0
    
    key = (curr_device, seen_dac, seen_fft)
    if key in visited2:
        return visited2[key]
    sum = 0
    for device in devices[curr_device]:
        sum += dfs2(device, end, devices, seen_dac, seen_fft)
    visited2[key] = sum
    return sum


def solution_one():
    file = read_file()
    sum = 0
    devices = {}
    for line in file:
        line = line.strip()
        tmp = line.split(' ')
        value = tmp[0][:len(tmp[0])-1]
        if value not in devices.keys():
            output_list = set()
            for i in range(1, len(tmp)):
                output_list.add(tmp[i])
            devices[value] = output_list
    start = 'you'
    end = 'out'
    sum = dfs1(start, end, devices)
    return sum

def solution_two():
    file = read_file()
    sum = 0
    devices = {}
    for line in file:
        line = line.strip()
        tmp = line.split(' ')
        value = tmp[0][:len(tmp[0])-1]
        if value not in devices.keys():
            output_list = set()
            for i in range(1, len(tmp)):
                output_list.add(tmp[i])
            devices[value] = output_list
    sum = dfs2('svr', 'out', devices, False, False)
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
