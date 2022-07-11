num_neg = -2123
num_zero = 0
num_pos = 123


def int2str(number: int):
    if number == 0:
        return '0'
    
    cur = ''
    if number < 0:
        out = '-'
        number *= -1
    else:
        out = ''

    while number > 0:
        i = number%10
        cur = chr(ord('0')+i) + cur
        number //= 10
    
    out += cur
    return out

print(int2str(num_neg))
print(type(int2str(num_neg)))
print(int2str(num_zero))
print(type(int2str(num_zero)))
print(int2str(num_pos))
print(type(int2str(num_pos)))

