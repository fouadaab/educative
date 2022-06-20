str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"

def recursive_upper(abc: str, n=0):
    if n >= len(abc) -1:
        return "no upper case letter in string"
    if abc[n].isupper():
        return abc[n]
    return recursive_upper(abc, n=n+1)

print(recursive_upper(str_1))
print(recursive_upper(str_2))
print(recursive_upper(str_3))

def recursive_upper_all(abc: str, out=None, n=0):
    if n==0 and not out:
        out = []
    if n >= len(abc) -1:
        return out
    if abc[n].isupper():
        out.append(abc[n])
    return recursive_upper_all(abc, out=out, n=n+1)

out = []
print(recursive_upper_all(str_1, out=out))
print(recursive_upper_all(str_2, out=out))
print(recursive_upper_all(str_3, out=out))