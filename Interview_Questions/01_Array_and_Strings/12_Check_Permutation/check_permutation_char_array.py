def check_permutaton(s:str, t:str)->bool:

    if len(s) != len(t):
        return False

    letters = [0 for _ in range(128)]

    for c in s:
        letters[ord(c)] += 1
    
    for c in t:
        letters[ord(c)] -= 1
        if letters[ord(c)] < 0:
            return False
    
    return True