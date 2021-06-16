def search (nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        pivot = left + (right-left)//2
        if nums[pivot] == target:
            return pivot
        if nums[pivot] < target:
            left = pivot+1
        if nums[pivot] > target:
            right = pivot -1 
    return -1

nums = [-1,0,3,5,9,12]
target = 9
a = search(nums, target)
print(a)