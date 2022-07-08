sentences = [
    'Live on time, emit no evil',
    'Was it a cat I saw',
    'Never odd or even',
    'radar',
]

def is_palindrome(sentence: str):
    s = ''.join([i for i in sentence if i.isalnum()]).lower()
    return s[:] == s[::-1]

def is_palindrome_dynamic(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        i += 1
        j -= 1
    return True

for sentence in sentences:
    print(f'{sentence} is palindrome: {is_palindrome_dynamic(sentence)}')