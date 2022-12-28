from collections import Counter

def verify_polindrome(s:str):

    s = s.replace(' ', '')
    s = ''.join(sorted(s))

    n = len(s)
    letters_counter = Counter(s)
    letters = letters_counter.keys()
    has_central = n%2 != 0
    count_central = False

    for letter in letters:
        letter_quant = letters_counter[letter]
        if letter_quant%2 != 0:
            if has_central and not count_central:
                count_central = True
            else:
                return False

    return True
