from collections import defaultdict
from typing import List

_hash = defaultdict(bool)
test_arr = [-2,1,2,4,7,11]
target = 13

# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(arr: List[int], target: int):
    for i in arr:
        if not _hash[i]:
            _hash[target-i] = True
        else:
            return True
    return False

# Time Complexity: O(n)
# Space Complexity: O(1)
# Assumes sorted list (asc)!
def two_sum_opt(arr: List[int], target: int):
  i = 0
  j = len(arr) - 1
  while i < j:
    if arr[i] + arr[j] == target:
      print(arr[i], arr[j])
      return True
    elif arr[i] + arr[j] < target:
      i += 1
    else:
      j -= 1
  return False

print(two_sum_hash_table(test_arr, target))
print(two_sum_opt(test_arr, target))