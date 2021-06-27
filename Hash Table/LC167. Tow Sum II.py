#binary search
def sum2(nums, target):
    n = len(nums)
    for i in range(n):
        low, high = i+1, n-1
        while low <= high:
            mid = (low+high) //2
        if nums[mid] == target - nums[i]:
            return [i+1, mid +1]
        elif nums[mid] > target - numbers[i]:
            high = mid - 1
        else:
            low = mid +1
    return [-1, -1]
#Time complixity: O(nlogn)


#two point
def sum22(nums, target):
    low, high = 0, len(nums) -1
    while low < high:
        total = nums[low] + nums[high]
        if total == target:
            return [low+1, high+1]
        elif total < target:
            low += 1
        else:
            high -= 1
    return [-1,-1]






