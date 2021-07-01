
#a common solution
def removeDuplicates(nums):
    def process(nums, k):
        idx = 0
        for x in nums:
            if idx < k or nums[idx-k]!= x:
                nums[idx] = x
                idx += 1
        return idx
    return process(nums, 1)

# two points solution
def removeDuplicates(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1# j represent seat, j +1 = length


