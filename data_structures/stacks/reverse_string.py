from stack import Stack

test_string = 'Hello'
my_stack = Stack()
reverse = ''

for i in test_string:
    my_stack.push(i)

while not my_stack.is_empty():
    reverse += my_stack.pop()
