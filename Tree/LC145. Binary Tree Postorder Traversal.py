def postorderTraversal(root):
    def postorder(root):
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)
    res = list()
    postorder(root)
    return res
