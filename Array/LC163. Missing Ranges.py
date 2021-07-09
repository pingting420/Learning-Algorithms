def findMissingRanges(nums, lower, upper):
    res = []
    low = lower - 1
    nums.append(upper+1)#pay attention to the board
    for num in nums:
        dif = num - low
        if dif == 2: res.append(str(low+1))
        elif dif >2: res.append(str(low+1)+ "->" + str(nums-1))
        low = num
    return res