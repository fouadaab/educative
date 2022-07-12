from typing import List, Union

def find_bitonic_peak(arr: List[int]) -> Union[int, None]:
    left = 0
    right = len(arr) - 1

    # Require at least 3 elements for a bitonic sequence.
    if len(arr) < 3:
        return None

    while left <= right:
        mid = (left + right)//2
        mid_left = max(0, mid-1)
        mid_right = min(len(arr)-1, mid+1)
        
        if arr[mid] > arr[mid_right] and arr[mid_left] > arr[mid]:
            right = mid - 1
        
        elif arr[mid_right] > arr[mid] and arr[mid] > arr[mid_left]:
            left = mid + 1
        
        else:
            return arr[mid]

    return None

def find_bitonic_peak_alt(arr: List[int]) -> Union[int, None]:
    left = 0
    right = len(arr) - 1

    # Require at least 3 elements for a bitonic sequence.
    if len(arr) < 3:
        return None

    while left <= right:
        mid = (left + right)//2
        mid_left = arr[mid - 1] if mid - 1 >=0 else float("-inf")
        mid_right = arr[mid + 1] if mid + 1 < len(arr) else float("inf")
        
        if mid_left < arr[mid] and mid_right > arr[mid]:
            left = mid + 1
        elif mid_left > arr[mid] and mid_right < arr[mid]:
            right = mid - 1
        elif mid_left < arr[mid] and mid_right < arr[mid]:
            return arr[mid]

    return None

arr0 = [1,2,3,4,5,4,3,2,1]
arr1 = [1,6,5,4,3,2,1]
arr2 = [6,5,4,3,2,1]
arr3 = [1,2,3,4,1]
arr4 = [1,2,3,4]

for arr in [arr0, arr1, arr2, arr3, arr4]:
    print(find_bitonic_peak(arr))