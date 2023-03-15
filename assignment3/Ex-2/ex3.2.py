import json
import time
import matplotlib.pyplot as plt
import numpy as np

# Load the array and the list of search tasks
with open('ex2data.json', 'r') as f:
    array = json.load(f)
with open('ex2tasks.json', 'r') as f:
    search_tasks = json.load(f)

# Standard binary search with configurable initial midpoint
def binary_search(array, value, start, end, initial_midpoint):
    if start > end:
        return -1
    mid = initial_midpoint
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search(array, value, mid+1, end, (mid+1+end)//2)
    else:
        return binary_search(array, value, start, mid-1, (start+mid-1)//2)

# Time the performance of each search task with different midpoints
results = []
for task in search_tasks:
    min_time = float('inf')
    best_mid = -1
    for i in range(len(search_tasks)):
        mid = np.random.randint(0, len(array) - 1)
        start = 0
        end = len(array) - 1
        start_time = time.time()
        result = binary_search(array, task, start, end, mid)
        end_time = time.time()
        search_time = end_time - start_time
        if search_time < min_time:
            min_time = search_time
            best_mid = mid
    results.append((task, best_mid, min_time))

# Produce a scatterplot visualizing each task and the corresponding chosen midpoint
values = [task[0] for task in results]
midpoints = [task[1] for task in results]
plt.scatter(values, midpoints)
plt.xlabel('Value')
plt.ylabel('Chosen Midpoint')
plt.show()