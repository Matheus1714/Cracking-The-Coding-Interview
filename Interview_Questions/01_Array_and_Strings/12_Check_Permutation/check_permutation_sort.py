def sort(s:str)->str:
    chs = list(s)
    chs.sort()
    return ''.join(chs)

def check_permutaton(s, t):

    if len(s) != len(t):
        return False
    return sort(s) == sort(t)