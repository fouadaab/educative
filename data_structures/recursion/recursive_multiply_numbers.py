x = 500
y = 2000

def recursive_multiply(x:int, y:int) -> int:
    # This cuts down on the total number of recursive calls:
    # N recursive calls with N = min(x,y)
    # Won't work when both x and y > limit of recursive calls
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(recursive_multiply(x, y))