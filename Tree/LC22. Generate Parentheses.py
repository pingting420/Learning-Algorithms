def generateParenthesis(self, n):
        
        
        res = []#to store the path
        cur_str = '' #to store the string path from root to leaf
        #In order to generate, we can use the recursion
        #the number of left should less than number of right
        #left the number of left pair can be ueds
        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                return res.append(cur_str)
            if right < left:
                return
            if left > 0:
                dfs(cur_str+'(', left -1, right)
            if right > 0:
                dfs(cur_str + ')', left, right-1)
        dfs(cur_str, n, n)
        return res
            