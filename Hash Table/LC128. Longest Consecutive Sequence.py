def longestConsecutive(nums):
    nums = set(nums)#transfer to a set
    #define a res
    res = 0
    for i in nums:
        if i-1 not in nums:
            #define the inint num
            tmp = 1
            while i + 1 in nums:
                res +=1
                tmp +=1
            res = max(tmp, res)
    return res 
    #res instore the largest num

#hashtable
def longestConsecutive2(nums):
    lookup = {}
    res = 0
    for num in nums :
        if num not in lookup:
            left = lookup[num -1] if num - 1 in lookup else 0
            right = lookup[num+1] if num + 1 in lookup else 0 
            lookup[num] = left + right +1
        #record the length
            lookup[num - left] = left + right +1
            lookup[num + right] = left + right +1
            res = max(res, left + right +1)
    return res 