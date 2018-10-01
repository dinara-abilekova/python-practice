"""
Implementation of Insertion Sort
"""
arr_size = int(input("Write array's size: "))

import random
arr = [random.choice([i for i in range(-1000, 1000)]) for j in range(arr_size)]
print("\nArray:")
print(arr)

for k in range(1, arr_size):
	key = arr[k]
	l = k - 1
	while l>=0 and arr[l]>key:
		arr[l+1] = arr[l]
		l -= 1
	arr[l+1] = key

print("\nSorted array:")
print(arr)