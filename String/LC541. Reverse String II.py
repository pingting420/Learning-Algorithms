def reverseStr(s,k):
    #first change the str to the list
    #use the range function
    #reversed function
    a = list(s)
    for i in range(0, len(s), 2*k):
        a[i:i+k] = a[i:i+k][::-1]
    return "".join(a)
#time complexity： O(N)
#use range(start, stop, step) to express from start to stop-1, step
#

