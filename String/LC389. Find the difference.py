def findTheDifference(s,t):
    s = Counter(s)
    t = COunter(t)
    for i in (t-s):
        return i

def findTheDifference(s,t):
    return list(Counter(t) - Counter(s))[0]

def findTheDifference(s,t):
    for i in set(t):
        if s.count(i) != t.count(i):
            return i
    