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
    print(nearest_neighbor(test_cases[i]))
    print(f"Time taken in seconds for case {i+1}: {time()-start_time:.5f}")