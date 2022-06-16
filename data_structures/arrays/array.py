from typing import List

def advance(a: List[int]):
    _max_reach = 0
    _idx = 0

    while _idx <= _max_reach < len(a):
        _max_reach = max(_max_reach, _idx + a[_idx])
        _idx += 1
    
    return _max_reach >= len(a)

winnable_array = [3, 3, 1, 0, 2, 0, 1]
unwinnable_array = [3, 2, 0, 0, 2, 0, 1]
print(advance(winnable_array))
print(advance(unwinnable_array))