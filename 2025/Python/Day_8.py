import math

def read_file():
    file = open('input.txt', 'r')
    return file

def euclidean_distance(x, y):
    return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2) + ((x[2] - y[2]) ** 2))


def solution_one():
    file = read_file()
    coordinates = []
    distances = []
    result = 1

    for line in file:
        line = line.strip()
        tmp = line.split(',')
        coordinates.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distances.append([i, j, int(euclidean_distance(coordinates[i], coordinates[j]))])
    distances = sorted(distances, key=lambda x: x[2])

    num_connections = 1000
    num_circuits = 3
    circuits = []
    for i in range(num_connections):
        found = False
        new_circuit = [distances[i][0], distances[i][1]]
        if circuits == []:
            circuits.append(new_circuit)
            continue
        for j in range(len(circuits)):
            if new_circuit[0] in circuits[j] and new_circuit[1] in circuits[j]:
                found = True
                break
            if new_circuit[0] in circuits[j]:
                found = True
                combined = False
                for k in range(j+1, len(circuits)):
                    if new_circuit[1] in circuits[k]:
                        combined_circuit = circuits[k] + circuits[j]
                        circuits[k] = []
                        combined = True
                        break
                if combined:
                    circuits[j] = combined_circuit
                else:
                    circuits[j].append(new_circuit[1])
                break
            elif new_circuit[1] in circuits[j]:
                found = True
                combined = False
                for k in range(j+1, len(circuits)):
                    if new_circuit[0] in circuits[k]:
                        combined_circuit = circuits[k] + circuits[j]
                        circuits[k] = []
                        combined = True
                        break
                if combined:
                    circuits[j] = combined_circuit
                else:
                    circuits[j].append(new_circuit[0])
                break
        if found:
            continue
        else:
            circuits.append(new_circuit)
    circuits.sort(key=len, reverse=True)
    for i in range(num_circuits):
        result *= len(circuits[i])
    return result
    
def solution_two():
    file = read_file()
    coordinates = []
    distances = []
    result = 0

    for line in file:
        line = line.strip()
        tmp = line.split(',')
        coordinates.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distances.append([i, j, int(euclidean_distance(coordinates[i], coordinates[j]))])
    distances = sorted(distances, key=lambda x: x[2])
    circuits = []
    line1 = 0
    line2 = 0
    for i in range(len(distances)):
        found = False
        new_circuit = [distances[i][0], distances[i][1]]
        if circuits == []:
            circuits.append(new_circuit)
            continue
        for j in range(len(circuits)):
            if new_circuit[0] in circuits[j] and new_circuit[1] in circuits[j]:
                found = True
                break
            if new_circuit[0] in circuits[j]:
                found = True
                combined = False
                for k in range(len(circuits)):
                    if new_circuit[1] in circuits[k]:
                        combined_circuit = circuits[k] + circuits[j]
                        circuits[k] = []
                        combined = True
                        break
                if combined:
                    circuits[j] = combined_circuit
                else:
                    circuits[j].append(new_circuit[1])
                break
            elif new_circuit[1] in circuits[j]:
                found = True
                combined = False
                for k in range(len(circuits)):
                    if new_circuit[0] in circuits[k]:
                        combined_circuit = circuits[k] + circuits[j]
                        circuits[k] = []
                        combined = True
                        break
                if combined:
                    circuits[j] = combined_circuit
                else:
                    circuits[j].append(new_circuit[0])
                break
        if len(circuits[0]) == len(coordinates):
            line1 = new_circuit[0]
            line2 = new_circuit[1]
            break
        if found:
            circuits.sort(key=len, reverse=True)
            continue
        circuits.append(new_circuit)
        circuits.sort(key=len, reverse=True)
    x1, x2, counter = -1, -1, 0
    file = read_file()
    for line in file:
        line = line.strip()
        tmp = line.split(',')
        if counter == line1:
            x1 = int(tmp[0])
        elif counter == line2:
            x2 = int(tmp[0])
        if x1 > -1 and x2 > -1:
            break
        counter += 1
    result = x1 * x2
    return result

if __name__ == '__main__':
    answer_one = solution_one()
    print(answer_one)
    answer_two = solution_two()
    print(answer_two)
