def threeSumClosest(nums,target):
    nums.sort()
    n = len(nums)
    res = float("inf")
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = i - 1
        while left < right:
            cur = nums[i] + nums[left] + nums[right]
            if cur == target:
                return target
            if abs(res - target) > abs(cur - target):#store cur and res,compare there result
                res = cur
            if cur > target:
                right -= 1
            elif cur < target:
                left +=1
    return res
#Time complexity: O(N2)
#Devide to three steps:
#nums[i] if equal to nums[i-1]
#nums[i] + nums[left] + nums[right] if equal to target
#if the res is the most propre 
