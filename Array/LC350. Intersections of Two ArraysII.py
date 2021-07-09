def intersect(nums1, nums2):
        nums1 = Counter(nums1)
        res = []
        for i in nums2:
            if i in nums1 and nums1[i]:
                res.append(i)
                nums1[i] -= 1#this way can avoid to calcualte twice,append and then minus 1
        return res

#Two points
def intersect2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    l1, l2 = 0,0
    res = []
    while l1 < len(nums1) and l2< len(nums2):
        if nums1[l1] == nums2[l2]:
            res.append(nums1[l1])
            l1 +=1
            l2 +=1
        elif nums1[l1]<nums2[l2]:
            l1 +=1
        else:
            l2 +=1
    return res