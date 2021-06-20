#soluton1
def intersection1(nums1, nums2):
    #define a set to sotre the res
    res = set()
    for i in nums2:
        if i in nums1:
            res.add()
    return res

#solution2 sort + two points
#step: sort two array
#we can use two points to traverse two arries
#we also should use pre to record the element add into the res
def intersection2(nums1, nums2):
    nums1.sort()#sort don't need to feed and variable
    nums2.sort()
    length1, length2 = len(nums1), len(nums2)#record the length of the element
    ins = list()
    index1 = index2 = 0
    while index1 < length1 and index2 < length2:
        nums1 = nums1[index1]
        nums2 = nums2[index2]
        if nums1 == nums2:
            if not ins or nums1 != index1[-1]:
                ins.append(nums1)
            index1 +=1
            index2 +=1
        elif nums1 < nums2:
            index1 +=1
        else:
            index2 +=1
    return ins

  '''
  l = []
nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                l.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]: j += 1
            else: i += 1
        return l#binary sesrch
        '''





