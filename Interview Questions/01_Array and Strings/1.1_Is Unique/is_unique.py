import unittest

def is_unique_chars(s:str):
    if len(s) > 128:
        return False

    char_set = 128 * [False]
    for ch in s:
        i = ord(ch)
        if char_set[i]:
            return False
        char_set[i] = True

    return True

print(is_unique_chars('1'))
print(is_unique_chars('12'))
print(is_unique_chars('11'))
print(is_unique_chars('123'))
print(is_unique_chars('123123'))
print(is_unique_chars('1234562'))