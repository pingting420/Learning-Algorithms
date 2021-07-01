def threeSum(nums):
    res_list = []
    nums.sort() #sort the result
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        #if after sorting and two numbers equal, then jump the loop
        if i >0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[j] + nums[k] == -nums[i]:
                res_list.append([nums[i],nums[j],nums[k]])
                while j <k and nums[j] == nums[j+1]:
                    j = j+1
                while j <k and nums[k] == nums[k-1]:
                    k = k-1
                j +=1
                k -=1
            elif nums[j] + nums[k] < -nums[i]:
                j = j+1
            else:
                k = k-1
    return res_list
            



