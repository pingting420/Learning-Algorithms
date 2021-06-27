def Nondecreasing(nums):
    N = len(nums)
    count = 0
    for i in range(1,N):
        if nums[i-1] > nums[i]:
            count += 1
            if i = 1 or nums[i] > nums[i+2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return count <=1