from collections import defaultdict

str1 = "rail safety"
str1_test = "fairy tales"
str2 = "roast beef" 
str2_test = "eat for BSE"

def is_anagram(str1: str, str2: str) -> bool:
    hash_ = defaultdict(int)
    for i in str1:
        if i.isalnum():
            hash_[i.lower()] += 1
    for i in str2:
        if i.isalnum():
            hash_[i.lower()] -= 1
    return max(hash_.values())==0
    

print(is_anagram(str1, str1_test))
print(is_anagram(str2, str2_test))