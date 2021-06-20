def isIsomorphic(s,t):
    s_map1 = {}
    t_map2 = {}
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    #define the range
    for i in range(s_len):
        if s_map1.get(s[i]) != t_map2.get(t[i]):
            return False
        s_map1[s[i]] = t_map2[t[i]] = i
    return True
        
