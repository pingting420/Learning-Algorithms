def fourSum(nums, target):
    #board situation
    if not nums or len(nums) < 4:
        return []
    #no matter to calculate sum of how many nums, the first step is to sort the nums
    nums.sort()
    res = [] #create a list to store res
    for a in range(len(nums) - 3):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        for b in range(len(nums) - 2):
            if b > a+1 and nums[b] == nums[b-1]:
                continue
        c = b+1
        d = len(nums) - 1
        while c < d:
            sum = nums[a] + nums[b] + nums[c] + nums[d]
            if sum == target:
                res.append([nums[a],nums[b],nums[c],nums[d]])
                while c < d and nums[c] == nums[c+1]:
                    c += 1
                while c < d and nums[d] == nums[d-1]:
                    d -= 1
                c +=1
                d -=1
            elif sum < target:
                c += 1
            else:
                d -= 1
        return res
