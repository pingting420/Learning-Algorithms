def reverseParentheses(self, s: str) -> str:
        #see tha pair should used to use stack
        #对于预处理括号的情况，如果遇到右括号就从右往左，如果遇到坐左括号，就从左往右
        stack = []
        n = len(s)
        pair= [0]*n
        
        #预先处理左右括号的映射关系
        for i in range(n):
            if s[i] == "(":#meet the "("
                stack.append(i)#put i into the stack
            if s[i] == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        index = 0
        #step = 1 表示向右走，stpr = -1表示向左走
        step = 1
        result = []
        while index < n:
            if s[index] == "(" or s[index] == ")":
                index = pair[index]
                step = -step
            else:
                result.append(s[index])
            index += step
        return "".join(result)