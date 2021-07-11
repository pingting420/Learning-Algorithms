def preorderTraversal(root):
        def preorder(root):
            if not root:
                return 
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = list()
        preorder(root)
        return res

from collections import deque
def aryTree(root):
    if not root:
        return []
    quene = deque([root])
    out_list = []

    while quene:
        in_list = []

        for _ in range(len(quene)):
            node = quene.popleft()
            in_list.append(node.val)
            if node.children:
                quene.extend(node.childre) #we should use extend here
        out_list.append(in_list)

    return out_list

                

    
    



    