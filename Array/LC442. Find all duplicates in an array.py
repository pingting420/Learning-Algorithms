def duplicates(nums):
    #travel all of the element, use two set to store them
    visited = set([])
    res = []
    for i in nums:
        if i not in visited:
            visited.add(i)
        else:
            res.append(i)
    return res
#we use add to add element for set
#we use append to add element fot list
