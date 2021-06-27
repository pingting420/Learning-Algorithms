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

    





