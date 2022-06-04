from inspect import stack
from stack import Stack

def convert_int_to_bin(dec_num):
    my_stack = Stack()
    bin_ = ''

    while dec_num > 0:
        my_stack.push(dec_num%2)
        dec_num = dec_num//2

    while not my_stack.is_empty():
        bin_ += my_stack.pop().__str__()

    return bin_

print(convert_int_to_bin(242))