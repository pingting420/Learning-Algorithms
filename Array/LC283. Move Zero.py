def moveZeros(nums):
    for num in nums:
        if num ==0:
            nums.remove(num)
            nums.append(num)