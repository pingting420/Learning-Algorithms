#Find the length of the list
#find the node of K+1
#K and K+1 devided, move to in the front of the list
def rotateList(head,k):
    if not head or head.next:return head
    Length = 0
    cur = head
    while cur:
        Length += 1
        cur = cur.next
    k %= Length
    if k == 0: return head
    #how to find the K+1, use fast and slow point:
    fast, slow = head, head
    for i in range(0,k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    #newHead is the Nth Node from end
    newHead = slow.next
    #devide the Node K+1 from the end and node K from the end
    slow.next = None
    fast.next = head
    return newHead
#Time complixity : O(N)
#Space complixity : O(1)
