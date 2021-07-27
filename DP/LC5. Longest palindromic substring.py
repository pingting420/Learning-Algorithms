#Solution1
#from the center extend to two sides

#first step
#to define a function to find the sub str

def longestPalindrome(s):
    n = len(s) 
    res = str()#res to put the answer
    if n<2: return s #if the length <2, return itself
    for i in range(n-1):
        #oddstr is the longest substring as i is the center
        oddstr = centerExtend(s,i,i)
        #evenstr is the longest sbustring as i and i+1
        evenstr = centerExtend(s,i,i+1)
        temp = oddstr if len(oddstr) > len(evenstr) else evenstr
        if len(temp) > len(res):res = temp
    return res

def centerExtend(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -=1
        right +=1
    #when jump out of the recursion, s[left] 1= s[right]
    return s[left+1:right]



