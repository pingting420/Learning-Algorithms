def validPalindrome(s):
    def checkPalindrome(low, high):#First to check if it palindrome
        i ,j = low, high
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low +=1
            high -=1
        else:
            return checkPalindrome(low+1, high) or checkPalindrome(low, high -1)
    return True
#Time complexity: O(N)