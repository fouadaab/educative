input_str = "LucidProgramming"

def recursive_len_str(input_str: str):
    if input_str == '':
        return 0
    return 1 + recursive_len_str(input_str[1:])

print(recursive_len_str(input_str))