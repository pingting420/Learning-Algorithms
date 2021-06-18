def reverseString(s):
        length = len(s)
        left, right = 0, len(s)-1
        while left < right:
            s[left] = s[right]
            left +=1
            right -=1
        return s

'''
def reverseString(s):
    for i in range(len(s)//2):
        s[i],s[-i-1] = s[-i-1],s[i]
'''
#know the structure, but if we want to get the index, first step is to define len(s)
s = reverseString(["h","e","l","l","0"])
print(s)