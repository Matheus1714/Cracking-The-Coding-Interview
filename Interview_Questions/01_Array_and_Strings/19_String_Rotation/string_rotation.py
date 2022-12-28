def is_rotation(s0:str, s:str)->bool:
    if len(s0) != len(s):
        return False
    
    xy = s0
    yx = s
    xyxy = xy + xy
    return yx in xyxy
    
