from functools import lru_cache

def read_file():
    file = open('input.txt', 'r')
    return file

def solution_two():
    file = read_file()
    total = 0
    edges = []
    cities = set()
    for line in file:
        a, rest = line.split(" to ")
        b, dist = rest.split(" = ")
        dist = int(dist)
        edges.append((a, b, dist))
        cities.add(a)
        cities.add(b)
    cities = list(cities)
    n = len(cities)
    city_to_idx = {city: i for i, city in enumerate(cities)}

    dist = [[float(0)] * n for _ in range(n)]
    for a, b, w in edges:
        i = city_to_idx[a]
        j = city_to_idx[b]
        dist[i][j] = w
        dist[j][i] = w 

    ALL_VISITED = (1 << n) - 1

    @lru_cache(None)
    def dfs(city, mask):
        if mask == ALL_VISITED:
            return 0
        best = float(0)
        for nxt in range(n):
            if not (mask & (1 << nxt)):
                best = max(
                    best,
                    dist[city][nxt] +
                    dfs(nxt, mask | (1 << nxt))
                )
        return best
    
    total = max(dfs(city_to_idx[city], 1 << city_to_idx[city]) for city in cities)
    return total

def solution_one():
    file = read_file()
    total = 0
    edges = []
    cities = set()
    for line in file:
        a, rest = line.split(" to ")
        b, dist = rest.split(" = ")
        dist = int(dist)
        edges.append((a, b, dist))
        cities.add(a)
        cities.add(b)
    cities = list(cities)
    n = len(cities)
    city_to_idx = {city: i for i, city in enumerate(cities)}

    dist = [[float('inf')] * n for _ in range(n)]
    for a, b, w in edges:
        i = city_to_idx[a]
        j = city_to_idx[b]
        dist[i][j] = w
        dist[j][i] = w 

    ALL_VISITED = (1 << n) - 1

    @lru_cache(None)
    def dfs(city, mask):
        if mask == ALL_VISITED:
            return 0
        best = float('inf')
        for nxt in range(n):
            if not (mask & (1 << nxt)):
                best = min(
                    best,
                    dist[city][nxt] +
                    dfs(nxt, mask | (1 << nxt))
                )
        return best
    
    total = min(dfs(city_to_idx[city], 1 << city_to_idx[city]) for city in cities)
    return total

if __name__ == '__main__':
    print(solution_one())
    print(solution_two())
