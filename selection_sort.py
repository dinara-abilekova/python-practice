"""
Implementation of Selection Sort
"""
arr_size = int(input("Write array's size: "))

import random
arr = [random.choice([i for i in range(-1000, 1000)]) for j in range(arr_size)]
print("\nArray:")
print(arr)

for k in range(arr_size-1):
	smallest = k
	for l in range(k+1, arr_size):
		if arr[l] < arr[smallest]:
			smallest = l
	arr[k], arr[smallest] = arr[smallest], arr[k]

print("\nSorted array:")
print(arr)

