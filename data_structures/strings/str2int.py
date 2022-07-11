num_neg = '-2123'
num_zero = '0'
num_pos = '123'


def str2int(string: str):
    
    out = 0
    if string[0] == '-':
        sign = -1
        string = string[1:]
    else:
        sign = 1

    for id,i in enumerate(list(reversed(string))):
        i = ord(i)-ord('0')
        out += i * 10**id
    
    out *= sign
    return out

print(str2int(num_neg))
print(type(str2int(num_neg)))
print(str2int(num_zero))
print(type(str2int(num_zero)))
print(str2int(num_pos))
print(type(str2int(num_pos)))

