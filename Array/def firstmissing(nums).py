def firstmissing(nums):
    if 1 not in nums:
        return 1
    for num in range(1, len(nums)+1):
        if num not in nums:
            return num
        return max(nums) + 1