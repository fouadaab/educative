from collections import deque

mock_array = [9,9,9]
out = deque()
# Add one to last decimal
carry = 1

# All decimals after first decimal
for i in mock_array[:0:-1]:
    if i+carry == 10:
        out.appendleft(0)
        carry = 1
    else:
        out.appendleft(i+carry)
        carry = 0

# Treat first decimal
if mock_array[0]+carry == 10:
    out.extendleft((0,1))
else:
    out.appendleft(mock_array[0]+carry)

print(out)
# returns deque([1, 0, 0, 0])