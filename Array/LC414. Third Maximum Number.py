#sort 
#loc:should consider the situation that the number smaller than 3
def thirdMax(nums):
    #set can help us delete the duplicte number
    nums = list(set(nums))
    nums.sort()
    if len(nums)<3:
        return nums[-1]
    else:
        return nums[-3]
