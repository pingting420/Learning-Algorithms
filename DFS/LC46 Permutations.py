def permute(nums):
    def backtrack(first = 0):
        #all number finish
        if first == n:
            res.append(nums[:])
        for i in range(first,n):
            nums[first],nums[i] = nums[i], nums[first]
            backtrack(first+i)
            nums[first],nums[i] = nums[i],nums[forst]
    n = len(nums)
    res = []
    backtrack()
    return res