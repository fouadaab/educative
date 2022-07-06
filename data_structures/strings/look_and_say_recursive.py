def next_number(s, m, i=1, j=0):
    if j == len(s)-1:
        return str(i)+m

    if m == s[j+1]:
        return next_number(s, m, i=i+1, j=j+1)
    else:
        return str(i)+m + next_number(s, s[j+1], i=1, j=j+1)

s = '1'
print(f'Init: {s}')
n = 5
for _ in range(n):
    s = next_number(s=s, m=s[0])
    print(f'Next: {s}')