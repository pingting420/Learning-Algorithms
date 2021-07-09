def countainsDuplicate(nums):
    return len(nums) != len(set(nums))

#return len(nums) - len(set(nums)) > 1