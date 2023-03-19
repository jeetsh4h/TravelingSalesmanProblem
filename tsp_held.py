from itertools import combinations

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


####################################################################################

import numpy as np
np.random.seed(42)


# 1, 2, 3
test_cases = [
    np.array([[0, 10, 15, 20], 
              [10, 0, 35, 25], 
              [15, 35, 0, 30],
              [20, 25, 30, 0]]),
    np.array([[0, 20, 42, 35, 25],
              [20, 0, 30, 34, 30],
              [42, 30, 0, 12, 10],
              [35, 34, 12, 0, 8],
              [25, 30, 10, 8, 0]]),
    np.array([[0, 10], 
              [10, 0]]),
]

# 4
distances = np.random.randint(1, 100, size=(10, 10))
distances = (distances + distances.T) / 2
np.fill_diagonal(distances, 0)

test_cases.append(distances)

# 5
distances = np.random.randint(1, 100, size=(15, 15))
distances = (distances + distances.T) / 2
np.fill_diagonal(distances, 0)

test_cases.append(distances)


from time import time

for i in range(len(test_cases)):
    start_time = time()
    print(f"Test {i + 1}:")
    print(held_karp(test_cases[i]))
    print(f"Time taken in seconds for case {i+1}: {time()-start_time:.5f}")