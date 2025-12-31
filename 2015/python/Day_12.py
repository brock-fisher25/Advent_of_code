def read_file():
    file = open('input.txt', 'r')
    return file

def process_input(input):
    total = 0
    c = 0
    while c < len(input):
        num = ''
        if input[c] == '-':
            num += '-'
            for i in range(c+1, len(input)):
                if input[i].isdigit():
                    num += input[i]
                    c += 1
                else:
                    break
        elif input[c].isdigit():
            num += input[c]
            for i in range(c+1, len(input)):
                if input[i].isdigit():
                    num += input[i]
                    c += 1
                else:
                    break
        if num != '':
            total += int(num)
        c += 1
    return total

def solution_two():
    file = read_file()
    for line in file:
        input = line.strip()
    # remove all red brackets
    final_input = ''
    c = 0
    bracket_stack = []
    bad_indices = []
    while c < len(input):
        if input[c] == '{':
            bracket_stack.append([c, False])
        elif input[c] == '}':
            start, has_red = bracket_stack.pop()
            if has_red:
                bad_indices.append([start, c])
        elif input[c:c+6] == ':"red"':
            if bracket_stack:
                bracket_stack[-1][1] = True
        c += 1
    bad_indices.sort(key=lambda x: x[0])
    final_bad_indices = []
    for start, end in bad_indices:
        if not final_bad_indices or start > final_bad_indices[-1][1]:
            final_bad_indices.append([start, end])
        else:
            final_bad_indices[-1][1] = max(final_bad_indices[-1][1], end)
    index = 0
    for start, end in final_bad_indices:
        final_input += input[index:start]
        index = end + 1
    final_input += input[index:]
    return process_input(final_input)

def solution_one():
    file = read_file()
    for line in file:
        input = line.strip()
    return process_input(input)

if __name__ == '__main__':
    print(solution_one())
    print(solution_two())
