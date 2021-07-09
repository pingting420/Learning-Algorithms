#hashtable can be used to check if one is in another
#List should transfer to set to calculate
def getInsert(headA, headB):
    s = set()
    while headA:
        s.add(headA)
        headA = headA.next
    while headB:
        if headB in s:
            return headB
        headB = headB.next
    return None

def getInsert(headA, headB):
    a,b = headA, headB
    while a!= b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a 



