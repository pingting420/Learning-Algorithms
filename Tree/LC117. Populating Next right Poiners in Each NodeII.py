def connect(root) :
        if not root:
            return None
        queue = [root]
        while queue:#Traversal every level
            length=len(queue)
            tail = None 
            for i in range(length):
                curnode = queue.pop(0)
                if tail:
                    tail.next = curnode
                tail = curnode
                if curnode.left:queue.append(curnode.left)
                if curnode.right:queue.append(curnode.right)
        return root

#we also can use link
def connect(root):
    if not root:
        return None
    first = root
    while first:#Traversal every level
        dummyHead = Node(None)#to create a virtual node for the next level
        tail = dummyHead#to maintain a tail point for the next level
        cur = first
        while cur:#traversal for the node of cur level
            if cur.left:
                tail.next = cur.left
                tail = tail.next
            if cur.right:
                tail.next = cur.right
                tail = tail.next
            cur = cur.next
        first = dummyHead.next
    return root