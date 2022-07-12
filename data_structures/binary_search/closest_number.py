from typing import List

arr1 = [1, 2, 4, 5, 6, 6, 8, 9]
target1 = 11

arr2 = [2, 5, 6, 7, 8, 8, 9]
target2 = 4

def binary_search_closest(arr: List[int], target: int):
    left = 0
    right = len(arr) - 1
    closest = None

    # Edge cases for empty list of list
    # with only one element:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    while left < right:
    
        mid = (right + left) // 2
        if arr[mid] == target:
            return target
        
        mid_right = min(len(arr)-1, mid+1)
        mid_left = max(0, mid-1)
        diff_left = abs(arr[mid_left] - target)
        diff_right = abs(arr[mid_right] - target)
        diff_mid = abs(arr[mid] - target)

        if diff_right > diff_left:
            closest = arr[mid_left] if diff_left <= diff_mid else arr[mid]
            right = mid_left
        else:
            closest = arr[mid_right] if diff_right <= diff_mid else arr[mid]
            left = mid_right
    
    return closest

print(binary_search_closest(arr1, target1))
print(binary_search_closest(arr2, target2))