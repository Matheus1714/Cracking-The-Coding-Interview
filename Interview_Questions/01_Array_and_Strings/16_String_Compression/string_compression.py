from typing import List, Tuple

def get_letters_group(s:str)->List[Tuple[str, int]]:

    n = len(s)

    letters = []
    count_consecutive = 0
    for i in range(n):
        count_consecutive += 1
                
        if i + 1 >= n or s[i] != s[i+1]:
            letter = (s[i], count_consecutive)
            letters.append(letter)
            count_consecutive = 0

    return letters

def get_formated_group(group:List[Tuple[str, int]])->str:
    formated_group = ''
    for element in group:
        formated_group += '{}{}'.format(element[0], element[1])
    return formated_group

def compress(s:str)->str:
    letters_group = get_letters_group(s)
    compressed = get_formated_group(letters_group)
    return compressed if len(compressed) < len(s) else s

