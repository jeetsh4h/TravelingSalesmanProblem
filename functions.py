from itertools import permutations, combinations

def brute_force(distances):
    n = len(distances)
    nodes = range(n)
    min_cost = float('inf')
    min_path = None
    for path in permutations(nodes):
        cost = 0
        for i in range(n - 1):
            cost += distances[path[i]][path[i + 1]]
        cost += distances[path[-1]][path[0]]
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_cost, min_path



def held_karp(distances):
    n = len(distances)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], 0)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distances[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distances[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    return opt, list(reversed(path))



def nearest_neighbor(distances):
    n = len(distances)
    nodes = set(range(n))
    path = [0]
    nodes.remove(0)
    while nodes:
        current = path[-1]
        nearest = None
        min_distance = float('inf')
        for node in nodes:
            if distances[current][node] < min_distance:
                nearest = node
                min_distance = distances[current][node]
        path.append(nearest)
        nodes.remove(nearest)
    cost = sum(distances[path[i]][path[i + 1]] for i in range(n - 1))
    cost += distances[path[-1]][path[0]]
    return cost, path