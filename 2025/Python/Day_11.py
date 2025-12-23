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

def dfs2(curr_device, end, devices, path):
    if end in devices[curr_device]:
        if 'dac' in path and 'fft' in path:
            return 1
        return 0
    if path in visited2:
        return visited2[path]
    if path == '':
        working_path = curr_device
    else:
        working_path = path + ',' + curr_device
    sum = 0
    for device in devices[curr_device]:
        sum += dfs2(device, end, devices, working_path)
    paths = working_path.split(',')
    path_to_record = ''
    for x in reversed(paths):
        path_to_record = x + ',' + path_to_record
        visited2[path_to_record] = sum
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
    start = 'svr'
    end = 'out'
    sum = dfs2(start, end, devices, '')
    return sum

if __name__ == '__main__':
 #   answer_one = solution_one()
  #  print(answer_one)
    answer_two = solution_two()
    print(answer_two)
