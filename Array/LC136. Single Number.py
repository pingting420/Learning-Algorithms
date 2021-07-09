def singleNumber(nums):
    L = set()
    for i in nums:
        if i in L:
            L.remove(i)
        else:
            L.add(i)
    return L.pop()

def singleNumber2(nums):
    for i in nums:
        count1 = nums.count(i)
        if count1 == 1:
            return i