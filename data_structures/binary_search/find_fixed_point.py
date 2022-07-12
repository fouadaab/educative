from typing import List, Union

def find_fixed_point(arr: List[int]) -> Union[int, None]:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == mid:
            return arr[mid]
        
        if arr[mid] < mid:
            left = mid+1
        else:
            right = mid-1
            
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]

for A in [A1,A2,A3]:
    print(find_fixed_point(A))