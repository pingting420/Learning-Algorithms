def rotate(nums,k):
    i = 1
    while i <= k:
        temp = nums[-1]
        nums = nums[0:-1]#from the first to the last second
        nums = [temp] + nums
        i = i+1


#“1234567”
#“7654321”
#“567 1234”
#“5671234
def rotate(A,k):
    def reverse(i,j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -=1
    n = len(A)
    k %= n
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

def rotate(nums,k):
    n = len(nums)
    k %= n 
    nums[:] = nums[-k:] + nums[:-k]

def rotate(nums,k):
    for i in range(k):
        nums = nums.insert(0,nums[-1])
        nums.pop



