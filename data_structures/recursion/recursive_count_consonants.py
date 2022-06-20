vowels = "aeiou"
input_str = "Welcome to Educative!"

def recursive_count_consonants(input_str: str, count=0, n=0):
    if n > len(input_str) - 1:
        return count
    if input_str[n].lower() not in vowels and input_str[n].isalpha():
        count+=1
    return recursive_count_consonants(input_str, count=count, n=n+1)

def recursive_count_consonants_alt(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])

print(recursive_count_consonants(input_str))
print(recursive_count_consonants_alt(input_str))