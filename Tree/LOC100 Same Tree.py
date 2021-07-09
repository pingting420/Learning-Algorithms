#DFS
def isSameTree(self, p, q):
    if not p or not q:
        return False
    elif not p and not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    