def countSubstrings(self,s):
    def speard(l ,r):
        count = 0
        while l>=0 and r<=len(s)-1 and s[l] = s[r]:
            l-=1
            r+=1
            count+=1
        return count
    ans = 0
    for i in range(len(s)):
        ans += speard(i,i)
    for i in range(len(s)-1):
        ans += speard(i,i+1)
    return ans