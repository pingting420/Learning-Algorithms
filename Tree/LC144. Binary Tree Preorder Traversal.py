#recursive
def preorderTraversal(root):
    def preorder(root):
        if not root:#结束的条件
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    res = list()
    preorder(root)
    return res 
#Time Complixity: O(N)

#Iterative
def preorderTraversal2(root):
    res = ()
    if not root:
        return res
    
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res
