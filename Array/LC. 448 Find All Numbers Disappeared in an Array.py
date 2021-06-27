def findDisappera(nums):
    new_nums = set(nums)
    return [n for n in range(1,len(nums)+1) if n not in new_nums]