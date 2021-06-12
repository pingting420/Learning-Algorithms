#using stack
def nextGreaterElement(nums1,nums2):
    dict_1 = {}
    stack = []

    for i in nums2[::-1]:
        while stack and stack[-1] <= i:
            stack.pop()
        
        if len(stack) == 0:
            dict_1[i] = -1
        else:
            dict_1[i] = stack[-1]
        
        stack.append(i)

    res = []
    for i in nums1:
        res.append(dict_1[i])
    return res

    nums1 = [1,2,5,6]
    nums2 = [1,2,5,6,7,8]
    a= nextGreaterElement(nums1, nums2)
    print(a)

