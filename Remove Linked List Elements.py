#Recrusion
def removeElements(head, val):
    if head is None:
        return head
    head.next = removeElements(head.next, val)
    if head.val == val:
        next_node = head.next
    else:
        next_node = head
    return next_node

#Iteration
#add dummy and use one more node to test the next val
def removeElements2(head, val):
    dummy = ListNode()
    dummy.next = head
    p = dummy
    while p is not None:
        if p.next and p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return dummy.next

