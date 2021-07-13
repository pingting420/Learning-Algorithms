#we can use move window
def lengthLongestSubstring(s):
    n = len(s)
    if n <= 1:return n
    max_len, window =0, set()
    left, right = 0,0
    while right < n:
        if s[right] not in window:
            max_len = max(max_len, right-left+1)
            window.add(s[right])
            right +=1
        else:
            window.remove(s[left])
            left+=1
    return max_len

    