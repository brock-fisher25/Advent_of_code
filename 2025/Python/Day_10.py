from collections import deque
from z3 import *

def read_file():
    file = open('input.txt', 'r')
    return file

def button_to_mask(indices, n):
    mask = 0
    for i in indices:
        mask |= 1 << (n - 1 - i)
    return mask

def fewest_presses(buttons, target_mask):
    start = 0
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        state, presses = queue.popleft()
        if state == target_mask:
            return presses
        for b in buttons:
            next_state = state ^ b
            if next_state not in seen:
                seen.add(next_state)
                queue.append((next_state, presses + 1))
    return None

def fewest_joltage_presses(buttons, final_joltages):
    m = len(buttons)
    n = len(final_joltages)

    presses = [Int(f"x{i}") for i in range(m)]

    opt = Optimize()

    for x in presses:
        opt.add(x >= 0)
    for j in range(n):
        opt.add(
            Sum(
                presses[i]
                for i in range(m)
                if j in buttons[i]
            ) == final_joltages[j]
        )
    opt.minimize(Sum(presses))

    if opt.check() == sat:
        model = opt.model()
        return sum(model[x].as_long() for x in presses)
    else:
        return None


def solution_one():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
        tmp = line.split(' ')
        buttons = []
        final_lights = []
        for i in tmp:
            if i[0] == '[':
                final_lights = list(i[1:len(i)-1])
                final_indices = []
                for j in range(len(final_lights)):
                    if final_lights[j] == '#':
                        final_indices.append(j)
            elif i[0] == '(':
                tmp = i[1:len(i)-1]
                new_button = []
                if ',' in tmp:
                    temp = tmp.split(',')
                    for k in temp:
                        new_button.append(int(k))
                else:
                    new_button = [int(tmp)]
                buttons.append(button_to_mask(new_button, len(final_lights)))
        sum += fewest_presses(buttons, button_to_mask(final_indices, len(final_lights)))
    return sum

def solution_two():
    file = read_file()
    sum = 0
    for line in file:
        line = line.strip()
        tmp = line.split(' ')
        buttons = []
        for i in tmp:
            if i[0] == '{':
                tmp = i[1:len(i)-1].split(',')
                final_joltages = []
                for k in tmp:
                    final_joltages.append(int(k))
            elif i[0] == '(':
                tmp = i[1:len(i)-1]
                new_button = []
                if ',' in tmp:
                    temp = tmp.split(',')
                    for k in temp:
                        new_button.append(int(k))
                else:
                    new_button = [int(tmp)]
                buttons.append(new_button)
        sum += fewest_joltage_presses(buttons, final_joltages)
    return sum

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
