def finMaxConsecutiveOnes(nums):
    count = max_count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(max_count, count)
    return max_count