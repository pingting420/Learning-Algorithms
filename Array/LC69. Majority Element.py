#using hash map
def majorityElement(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key = counts.get)
#Count.get can get the value, then xounts.keys() can get the biggest key