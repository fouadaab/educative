def next_number(s: str):
    if len(s) == 0:
        raise ValueError('Please insert a non-empty string')
    cur = s[0]
    out = ''
    j=1
    if len(s) == 1:
        return str(j)+cur
    for i in s[1:]:
        if i != cur:
            out += ''.join(str(j)+cur)
            cur = i
            j = 1
        else:
            j+=1
    out += ''.join(str(j)+cur)
    return out

init_ = '1'
n = 5
for _ in range(n):
    init_ = next_number(init_)
    print(init_)


