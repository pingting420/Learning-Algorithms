#first sloution
def findKthLargest1(nums):
    size = len(nums)
    nums.sort()
    return nums[size - k]


#second solution Quick sort
import random
def findKthLargest2(nums):
    return quickSort(nums,0,len(nums)-1,k)

def quickSort(nums,l,r,k):
    index = randomPartition(nums, l, r)
    if index == k-1:
        return nums[index]
    else:
        if index > k-1:
            return quickSort(nums,l,index-1,k)
        else:
            return quickSort(nums, index+1, r, k)

def randomPartition(nums, l, r):
    i = random.randint(l,r)
    nums[i], nums[r] = nums[r],nums[i]
    return partition(nums, l, r)

def partition(nums, l, r):
    pivot = nums[r]
    rightmost = r
    while l<=r:
        while (l <= r and nums[l] > pivot):
            l = l+1
        while (l <= r and nums[r] <= pivot):
            r = r-1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[rightmost] = nums[rightmost], nums[l]
    return l


        

    #third sloution Heap sort
from heapq import heapify, heappush, heappop
def findKthLargest3(nums):
    minheap = []
    heapify(minheap)
    for num in nums:
        heappush(minheap,num)
        if len(minheap) > k:
            heappop(minheap)
    return minheap[0]







