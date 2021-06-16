def searchInsert(nums, target):
    if target <= nums[0]:
            return 0
    if target > nums[len(nums)-1]:
            return len(nums)
    low, high = 0, len(nums)-1
    while low <= high:
            mid = (low+high) //2

            if target<nums[mid]:
                high = mid-1
            elif target >nums[mid]:
                low = mid+1
            else:
                return mid
            if target < nums[mid]:
                return mid
            if target > nums[mid]:
                return mid+1
