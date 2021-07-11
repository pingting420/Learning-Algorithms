class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def Inorder(root):
            if not root:
                return 
            Inorder(root.left)
            res.append(root.val)
            Inorder(root.right)
        res = list()
        Inorder(root)
        return res