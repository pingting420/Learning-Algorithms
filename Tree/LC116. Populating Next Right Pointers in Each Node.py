import collections
def connect(root):
        if not root:
            return root
        # put the first level node into the queue
        Q = collections.deque([root])
        
        # While using to iterative the level
        while Q:
            size = len(Q) #record the size of the Q
            #traversal all of the node in this level
            for i in range(size):
                #pop the element from the head of Q
                node = Q.popleft()
                #connect
                if i <size-1:
                    node.next = Q[0]
                
                #for the next level:
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root