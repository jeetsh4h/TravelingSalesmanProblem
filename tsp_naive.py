from itertools import permutations

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

for i in range(len(test_cases) - 1):    # the last test case takes too long to run
    start_time = time()
    print(f"Test {i+1}:")
    print(brute_force(test_cases[i]))
    print(f"Time taken in seconds for case {i+1}: {time()-start_time:.5f}")