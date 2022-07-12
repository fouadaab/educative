from typing import List

data = [0,1,1,2,5,6,9,11,12,33,34,35,65,99]
target = 5

def linear_search(data: List[int], target: int):	
	for i in range(len(data)):
		if data[i] == target:
			return True
	return False

print(linear_search(data, target))  # True

def binary_search_iterative(data: List[int], target: int):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False 

print(binary_search_iterative(data, target))

def binary_search_recursive(data: List[int], low: int, high: int, target: int):
    if low == high:
        return data[low] == target

    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        high = mid - 1
    else:
        low = mid + 1
    return binary_search_recursive(data, low, high, target)

print(binary_search_recursive(data, low=0, high=len(data)-1, target=target))