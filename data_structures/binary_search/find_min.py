from typing import List, Union

# def find(A: List[int]) -> Union[int, None]:
#     if len(A)==0:
#         return None
#     elif len(A)==1:
#         return A[0]
    
#     low = 0
#     high = len(A) - 1
#     left = A[low]
#     right = A[high]

#     while low <= high:
#         mid = (low + high) // 2
#         mid_right = min(len(A)-1, mid+1)
#         mid_left = max(0, mid-1)
        
#         if A[mid_right] > A[mid] and A[mid] > A[mid_left]:
#             if left > right:
#                 low = mid_right
#             else:
#                 high = mid_left

#         elif A[mid_right] < A[mid] and A[mid] > A[mid_left]:
#             return A[mid_right]
        
#         else:
#             return A[mid]
            
#     return None

def find(A: List[int]) -> int:
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low

A0 = [4, 5, 6, 7, 1, 2, 3]
A1 = [1, 2, 3, 4, 5, 6, 7]
A2 = [2, 3, 4, 5, 6, 7, 1]

for A in [A0,A1,A2]:
    print(find(A))