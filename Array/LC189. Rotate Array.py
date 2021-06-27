def rotate(nums):
    i = 1
    while i <= k:
        temp = nums[-1]
        nums = nums[0:-1]
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




