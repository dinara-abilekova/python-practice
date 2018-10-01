"""
Implementation of Merge Sort
"""
def merge_sort(arr):
	if len(arr) <= 1:
		return(arr)
	middle = len(arr) // 2
	left = merge_sort(arr[:middle])
	right = merge_sort(arr[middle:])
	return(merge(left, right))

def merge(left, right):
	result = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]
	if len(left) > 0:
		result += left
	if len(right) > 0:
		result += right
	return(result)

arr_size = int(input("Write array's size: "))

import random
arr = [random.choice([i for i in range(-1000, 1000)]) for j in range(arr_size)]
print("\nArray:")
print(arr)

print("Sorted array:")
sorted_arr = merge_sort(arr)
print(sorted_arr)