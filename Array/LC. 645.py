def finErrorNums(nums):
    n = len(nums)
    repeat = sum(nums) - sum(set(nums))
    missing = repeat +int(n*(n+1)/2) - sum(nums)
    return [repeat, missing]