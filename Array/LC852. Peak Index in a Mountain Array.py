#Traversal
def peakIndexInMountainArray(arr):
    n = len(arr)
    ans = 0
    for i in (1,n-1):
        if arr[i] > arr[i+1]:
            ans = i
            break
    return ans
        
        #i is the index

#Binary Search

def PeakIndexInMountainArray2(arr):
    n = len(arr)
    left = 1
    right = n-2
    ans = 0
    while left <= right:
        mid = (right+left)//2
        for i in range(1,n-1):
            if mid[i]>mid[i+1]:
                ans = i
                right = mid-1
            else:
                left= mid+1
    return ans
