def new_ord(chr):
    int_ = ord(chr) - ord('A') + 1
    return int_

input_ = 'ZZ'
res_ = 0
for id,i in enumerate(reversed(input_)):
    res_ += new_ord(i)*26**id
print(res_)