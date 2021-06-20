# Calcualte the number, using hash table
# Using set to test if there any duplicate
#use append to add element into the hashtable
def containsDuplicate1(nums):
    hashtable = {}
    for i in nums:
        if not i in hashtable: hashtable.append(i)
        else: return True
    return False

#Another solution:compare the length
def containsDuplicate2(nums):
    nset = set(nums)
    if len(nset) < len(nums):
        return True
    return False

    
