from typing import List, Union

def find_first_entry(arr: List[int], target: int) -> Union[int, None]:
    '''
    In the worst case you can have an element or an array
    consisting of all elements of the same number
    and thus this approach will boil down to giving you 
    the same runtime as the initial naive approach
    '''
    left = 0
    right = len(arr) - 1

    # Edge cases for empty list of list
    # with only one element:
    if len(arr) <= 1:
        return None

    while left <= right:
    
        mid = (right + left) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            if mid - 1 < 0 or arr[mid - 1] < target:
                return mid
            right = mid - 1
    
    return None


arr = [-14, -10, -10, -10, 2, 107, 108, 108, 243, 285, 285, 285, 401, 401, 401, 401]
target = 285
print(find_first_entry(arr, target))