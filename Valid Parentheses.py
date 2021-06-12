def isValid(s):
    #using hash map
    op_map = {"{":"}","[":"]","(":")"}
    #define a stack
    stack = []
    for ch in s:
        if ch in op_map:
            stack.append(op_map[ch])
        elif not stack or (stack and stack.pop != ch):
            return False
    
    return not stack