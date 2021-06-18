#The first step is to compare the length
def isAnagram(s,t):
    return collections.Counter(s) == collections.Counter(t)


def isAnagram(s,t):
    ss = ','.join(sorted(s))
    tt = ','.join(sorted(t))
    if ss == tt:
        return(True)
    else:
        return(False)