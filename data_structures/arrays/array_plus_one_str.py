mock_array = [2,3,9,9]
out = ''
carry = 1

for i in mock_array[:0:-1]:
    if i+carry == 10:
        out = str(0) + out
        carry = 1
    else:
        out = str(i+carry) + out
        carry = 0

out = str(mock_array[0]+carry) + out

print(out)
# returns '2400'