class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildtree(preorder_left:int, preorder_right:int, inorder_left:int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left #the first node of preorder is root
            inorder_root = index[preorder[preorder_root]]#to find the index of root
            #build the root
            root = TreeNode(preorder[preorder_root])
            #to find the number of left node
            size_left_subtree = inorder_root - inorder_left
            #recursion to build the left tree, and connect to the root
            root.left = myBuildtree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
          
            root.right = myBuildtree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildtree(0, n - 1, 0, n - 1)

        