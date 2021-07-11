def levelOrderBottom(root):
        if not root:
            return
        result_list = []
        quene = [root]
        
        while quene:
            order_list = []
            for _ in range (len(quene)):
                cur_node = quene.pop(0)
                order_list.append(cur_node.val)
                if cur_node.left:
                    quene.append(cur_node.left)
                if cur_node.right:
                    quene.append(cur_node.right)
            result_list.append(order_list)
        result_list.reverse()
        return result_list

                