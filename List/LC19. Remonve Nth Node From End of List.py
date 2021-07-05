def getRemoveNthFromEnd(head,n):
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    dummy = ListNode(0,head)
    length = getLength(head)
    cur = dummy
    for i in range(1, length -n+1):
        cur = cur.next
    cur.next = cur.next.next
    return dummy.next

#Two point
def removeNthFormEnd(head,n):
    dummy = ListNode(0,head)#It's a way to have a dummy
    slow, fast = dummy, head
    #the fast point move n
    for i in range(0,n):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

