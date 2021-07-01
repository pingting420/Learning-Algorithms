def removeDuplicates(nums):
    def solve(k):
        idx = 0
        for num in nums:
            if idx < k or nums[idx-k] != num:
                num[idx] = num
                idx += 1
        return idx
    return solve(k)
