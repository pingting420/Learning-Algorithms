#Remove the element, wo should let head to next head
#We should design a virtual head, like dummy node.
def removeElements(head, val):
    dummy_head = ListNode(next = head) #add a virtual node
    cur = dummy_head #use dummy_head as cur
    while (cur.next != None):
        if (cur.next.val == val):
            cur.next = cur.next.next #delete the cur.next
        else:
            cur = cur.next
    return dummy_head.next

