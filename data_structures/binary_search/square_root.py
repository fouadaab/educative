def integer_square_root(k: int):
    if k <= 1:
        return k
    
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2

        if mid*mid > k:
            high = mid - 1

        elif mid*mid < k:
            low = mid + 1

        # Adding else to optimize
        # solution in time
        else:
            return mid
        
    return low - 1

k0 = 300
k1 = 12
k2 = 25

for k in [k0,k1,k2]:
    print(k)
    print(integer_square_root(k))