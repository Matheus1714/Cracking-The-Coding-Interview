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

import unittest

