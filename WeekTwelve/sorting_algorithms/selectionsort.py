import time
import random


def selection_sort(arr):
   n = len(arr)
   for i in range(n):
       min_index = i
       for j in range(i + 1, n):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]




array_sizes = [100, 200, 400, 800, 1600, 3200, 6400]  # Sizes of arrays to test


fastest_time = float('inf')
slowest_time = float('-inf')
fastest_size = None
slowest_size = None
total_time = 0
total_times = []


for size in array_sizes:
   total_times = []  # Store the time taken for each run
   print(f"\nArray Size: {size}")
   for _ in range(5):  # Repeat the sorting process 5 times for each array size
       arr = [random.randint(0, 1000) for _ in range(size)]
       start_time = time.time()
       selection_sort(arr)
       end_time = time.time()
       time_taken = end_time - start_time
       total_times.append(time_taken)  # Store the time taken for this run
       print(f"Run {len(total_times)}: Time taken: {time_taken:.6f} seconds")
  
   if time_taken < fastest_time:
       fastest_time = time_taken
       fastest_size = size
   if time_taken > slowest_time:
       slowest_time = time_taken
       slowest_size = size
   total_time += time_taken
   total_times.append(total_time)  # Store the total time for this array size
   print(f"Array size: {size}, Time taken: {time_taken:.6f} seconds")


   average_time = sum(total_times) / len(total_times)




print(f"\nFastest time: {fastest_time:.6f} seconds (Array size: {fastest_size})")
print(f"Slowest time: {slowest_time:.6f} seconds (Array size: {slowest_size})")
print(f"Average time: {average_time:.6f} seconds")