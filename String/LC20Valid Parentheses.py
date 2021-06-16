
#an easy understanding sloution
def isValid2(s):
    #check if the s is null
    if len(s) == 0:
        return True
    #create a stack
    stack = []
    #then begin to see
    for c in s:
        if c=='(' or s=="[" or c=="{":
            stack.append(c)
        #else means other situations
        else:
            temp =  stack.pop()
            if c == ")":
                if temp != "(":
                    return False
            elif c == "]":
                if temp != "[":
                    return False
            elif c == "}":
                if temp != "{":
                    return False
    return True if len(stack) == 0 else False
                





#solution2 using hashmap
def isValid2(s):
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