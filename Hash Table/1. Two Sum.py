def twoSum1(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def twoSum2(nums, target):
    dict_nums = dict()
    for index, value in enumerate(nums):
        reminder = target - value
        if reminder in dict_nums:
            return [dict_nums[reminder],index]
        dict_nums[value] = index

