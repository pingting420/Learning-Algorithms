#hashtable
def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True 
        seen.add(head)
        head = head.next
    return False



#two point
#slow and fast point
def hasCycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or fast.next:
            return False
        slow =slow.next
        fast = fast.next.next
    return True

