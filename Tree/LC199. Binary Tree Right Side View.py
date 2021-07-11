#Simliar to the inorder traveral, but traversal every level, need to check if it is the last element
from collections import deque
def BinaryTreeright(root):
    if not root:
        return []
    quene = deque([root])
    out_list = []
    
    while quene:
        node = quene[-1]#every time to pop the last node # this is the difference between inorder traversal
        out_list.append(node.val)

        #how to get all of the node of next level:
        for _ in range(len(quene)):
            node = quene.popleft()
            if node.left:
                quene.append(node.left)
            if node.right:
                quene.append(node.right)
    return out_list


