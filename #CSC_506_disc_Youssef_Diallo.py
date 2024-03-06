#CSC 506
# Bubble sort

import matplotlib.pyplot as plt
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

# Generate random data for sorting and measure the time taken by each algorithm
sizes = [100, 1000, 1500, 3000, 4000]
bubble_sort_times = []
cocktail_sort_times = []

for size in sizes:
    data = list(range(size, 0, -1))
    
    start_time = time.time()
    bubble_sort(data.copy())
    bubble_sort_times.append(time.time() - start_time)
    
    start_time = time.time()
    cocktail_sort(data.copy())
    cocktail_sort_times.append(time.time() - start_time)

# Plotting the performance comparison graph
plt.plot(sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(sizes, cocktail_sort_times, label='Cocktail Sort')
plt.xlabel('Number of Elements in List')
plt.ylabel('Time Taken (s)')
plt.title('Performance Comparison: Bubble Sort vs. Cocktail Sort')
plt.legend()
plt.show()