def containsNearbyDuplicate(nums, k):
    record = dict()
    for index, i in enumerate(nums):
        if i not in record: record[i] = index
        elif abs(record[i] - index) <= k:
            return True
        else: record[i] = index 
    return False