import re

def replace_spaces(s:str)->str:
    rt='%20'
    s = s.strip()
    return re.sub(r'\s+', rt, s)