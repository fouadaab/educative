from collections import defaultdict

def is_palindrome_permutation(str1: str):
    hash_ = defaultdict(int)
    count = 0
    for i in str1:
        if i.isalnum():
            hash_[i.lower()] += 1
            
    for j in hash_.values():
        count += j%2
        if count > 1:
            return False
    return True

str1 = 'tacocat'
print(is_palindrome_permutation(str1))
