#len - i <= citations[i]
# 0,1,3,5,6
#Binary search
def hIndex(citations):
    if not citations:
        return 0
    left = 0
    right = min(len(citations), max(citations))
    ans = 0
    def helper(k):
        cnt = 0
        for num in citations:
            if k <= num:
                cnt += 1
            return cnt
    while left <= right:
        mid = left + (right - left) //2
        cnt = helper(mid)
        if cnt < mid:
            right = mid-1
        else:
            ans = max(ans, mid)
            left = mid + 1
    return ans 

#more easy solution
def hIndex2(citations):
    C = sorted(citations, reverse = True)
    for h in range(len(C)):
        if h+1 > C[h]:
            return h
    return len(C)

#sloution3
def hIndex3(citations):
    n = len(citations)
    l, r = 0, n
    #board solution
    while l < r:
        mid = (l + r)//2
        if citations[mid] >= n - mid:
            r = mid
        else:
            l = mid +1
    return n - l