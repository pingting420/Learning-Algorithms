#DFS

def averageOfLevels(self, root: TreeNode) -> List[float]:
            counts = list()
            totals = list()
            def dfs(root,level):
                if not root:
                    return
                if level<len(totals):
                    totals[level] += root.val
                    counts[level] += 1
                else:
                    totals.append(root.val)#totals to store the sum
                    counts.append(1)#counts to store the level
                dfs(root.left,level+1)
                dfs(root.right,level+1)
            dfs(root,0)
            return[total/count for total, count in zip(totals,counts)]

#BFS

def averageLevels2(root):
    average = list()#store the average in a list
    queue = collections.deque([root])#store the average level root in a queue
    while queue:#when queue not euqal to zero
        total = 0
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()#先让左边的出来
            total + node.val#开始计算和
            left, right = node.left, node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        average.append(total/size)
    return average
