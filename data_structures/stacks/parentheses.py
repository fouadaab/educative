from stack import Stack

my_stack = Stack()
_hasher = {
    ']': '[',
    '}': '{',
    ')': '(',
}
test = '[][]'

for id, i in enumerate(test):

    # Edge case
    if id==0 and i in _hasher.keys():
        raise ValueError("Stack Not Balanced")

    # Push in stack while open parenthesis
    if i in _hasher.values():
        my_stack.push(i)

    # Pop last if closed parenthesis and assert if still balanced
    else:
        if my_stack.peek() != _hasher[i]:
            raise ValueError("Stack Not Balanced")
        my_stack.pop()
        
assert my_stack.is_empty(), "You thought so? Eat some Corsi Salt"