#We can devide the array into front and end
#in front store not equal to val, and back store equal to val.
def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1,2,3,3,4,5,6]
val = 4
a = removeElement(nums, val)
print(a)

def removeElement2(num, val):
    idx = 0
    for num in nums:
        if num!= val:
            nums[idx] = num
            idx += 1
    return idx

a = removeElement2(nums, val)
print(a)




    
    
    
    
    
    
    
    
'''
    if nums == None or len(nums) == 0:
        return 0
    #two points
    l, r = 0, len(nums) - 1
    #if l = r
    while l < r:
        while(l < r and nums[l] != val):
            l += 1
        while(l < r and nums[r] == val):
            r -=1
'''



