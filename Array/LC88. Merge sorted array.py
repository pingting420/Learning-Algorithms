def merge(nums1, nums2, m, n):
    nums1[:m] = nums2 #to put nums2 into the end of nums1
    nums1.sort()
# O(m+nlog(m+n))

#Two points
def merge2(nums1, nums2, m, n):
    sorted = []
    p1, p2 = 0, 0
    while p1<m and p2<n:
        if nums1[p1]<nums2[p2]:
            sorted.append(nums1[p1])
            p1+=1
        elif nums1[p1]>nums2[p2]:
            sorted.append(nums2[p2])
            p2 +=1
        elif p1 == m:
            sorted.append(nums2[p2])
            p2+=1
        else:
            sorted.append(nums1[p1])
            p1+=1
    nums1[:] = sorted





#define p1 and p2 as the head point of two nums
