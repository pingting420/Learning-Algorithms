#There are three useful function
#filter
# (str.isalnum,s)
#join function
#lower()

def Palindrome(s):
    s = ''.join(filter(str.isalnum,s)).lower()
    return s == s[::-1]

#solution2 , two points
def Palindrome(s):
    s = ''.join(filter(str.isalnum,s)).lower()
    len_s = len(s)
    left, right = 0, len_s-1
#broad situation
    while left<right:
        if s[left] != s[right]:
            return False
        left, right = left+1, right-1
    return True
        

