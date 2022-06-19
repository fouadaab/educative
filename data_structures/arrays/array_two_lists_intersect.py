from typing import List

# Two sorted lists
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
intersect = set()
intersect_list = list()

def intersect_sorted_array_set(A: List[int], B: List[int]):
    i=0
    j=0
    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            intersect.add(A[i])
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        elif B[j]<A[i]:
            j+=1
    return intersect

def intersect_sorted_array_list(A: List[int], B: List[int]):
    i=0
    j=0
    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersect_list.append(A[i])
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        elif B[j]<A[i]:
            j+=1
    return intersect_list

print(intersect_sorted_array_set(A, B))
print(intersect_sorted_array_list(A, B))