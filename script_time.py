from functions import nearest_neighbor, held_karp, brute_force

import numpy as np
from time import time
from statistics import mean

functions = [nearest_neighbor, held_karp, brute_force]


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



for func in functions:
    times = []
    for _ in range(3):
        start_time = time()
        for test in test_cases:
            func(test)
        times.append(time() - start_time)

    print(f"{func.__name__} algorithm took {mean(times)} seconds to run")
