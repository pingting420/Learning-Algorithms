def largestValues(root):
        if root is None:
            return []
        queue = [root]
        out_list = []
        while queue:
            length = len(queue)
            in_list = []
            for _ in range(length):
                curnode = queue.pop(0)
                in_list.append(curnode.val)
                if curnode.left: queue.append(curnode.left)
                if curnode.right: queue.append(curnode.right)
            out_list.append(max(in_list))
        return out_list
