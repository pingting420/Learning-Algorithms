def isSubsequence(s,t):
    list_t = list(t)
    list_s = list(s)
    #use an index to record the location
    for i in list_s:
        if i in list_t:
            index = list_t[index]
            list_t = list_t[index+1:]
        else:
            return False
    return True

#Two Point
def isSubsequence2(s,t):
    n, m =len(s),len(t)
    i = j =0
    while i<n and j<m:
        if s[i]==t[j]:
            i+=1
        j+=1
    return i == n
