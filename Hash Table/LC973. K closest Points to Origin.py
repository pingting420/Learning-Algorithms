#Solution1 Sort
def KClosest(points, k):
    points.sort(key = lambda x:(x[0]**2 + x[1]**2))
    return points[:k]
#Time complexity: O(nlogn)



