def findPairs(nums):
    res = 0
    c = collections.Counter(nums)
    for i in c:
        if k >0 and i+k in c or k ==0 and c[i]>1:#if k ==0, we should consider the num of c[i]>1
            res +=1
    return res 