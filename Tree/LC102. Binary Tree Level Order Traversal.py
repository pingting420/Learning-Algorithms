def levelOrder(root):
    if not root:
        return []
    
    quene = [root]#put the root into the queue
    out_list = []#the array of return

    while quene:
        length = len(quene)
        in_list = []#to store every level array
        for _ in range(length):
            curnode = quene.pop(0)#pop 0 
            in_list.append(curnode.val)#and into the nums
            if curnode.left : quene.append(curnode.left)#left and right into the queue
            if curnode.right : quene.append(curnode.right)
        out_list.append(in_list)
    return out_list

