#Solution:
#step1:calcualte the degree of the array--#hashtable: key:element, value:number
#step2:calcualte the shortest array
#using counter to store the numbers, than counter.values() = degree
#an important problem, can teach how to use enumerate, hashtable, counters,


def finddegree(nums):
    left, right = dict(), dict()
    counter = Counter(nums)
    for i, num in enumerate(nums):
        if num not in left:
            left[num] = i
        right[num] = i
        counter[num] += 1
    degree = max(counter.values())
    res = len(nums)
    for k, v in counter.items():
        if v == degree:
            res = min(res,right[k] - left[k] +1)
    return res


#use two dict to record the first time and last time 


def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        degree = max(cnt.values())
        dici, dicj = {}, {}
        for idx, num in enumerate(nums):
            if num not in dici:
                dici[num] = idx
            dicj[num] = idx
        res = len(nums)
        for key in cnt:
            if cnt[key] == degree:
                res = min(res, dicj[key] - dici[key] + 1)
        return res
