from collections import defaultdict

def is_unique_dict(input_str: str):
    hash_ = defaultdict(int)
    for i in input_str:
        if i.isalnum():
            hash_[i.lower()] += 1
        if hash_[i.lower()] > 1:
            return False
    return True

def is_unique_set(input_str):
    return len(set(input_str)) == len(input_str)

str1 = 'abCDefGh'
str2 = 'nonunique'
print(is_unique_set(str1))
print(is_unique_set(str2))