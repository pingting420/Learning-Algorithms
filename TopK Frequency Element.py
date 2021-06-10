#directly sort if k = 2
import collections
def topKFrequent1(nums):
    count = collections.Counter(nums)
    return [ item[0] for item in count.most_common(2)]#Why here is item[0]

a = topKFrequent1([2,2,2,3,3,4,5])
print(a)

#heap sort(1)
import collections
import heapq
def topKFrequent2(nums):
    count = collections.Counter(nums)
    heap = [(val,key) for key, val in count.items()]
    return [item[1] for item in heapq.nlargest(2,heap)]

a = topKFrequent2([2,2,2,3,3,4,5])
print(a)


# heap sort (2)
import collections
import heapq
def topKFrequent3(nums):
    count = collections.Counter(nums)
    heap = []
    for key, val in count.items():
        if len(heap) >= k:
            if val > heap[0][0]:
                heapq.heapreplace(heap, (val,key))
        else:
            heapq.heappush(heap, (val,key))
    return [item[1] for item in heap]

a = topKFrequent2([2,2,2,3,3,4,5])
print(a)




