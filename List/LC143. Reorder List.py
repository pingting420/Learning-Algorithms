def reorderList(self, head) :
        if not head:
            return 
        vec = list()#transfer the list to the vec, bucause list don't support visit by the index
        node = head
        while node:
            vec.append(node)
            node = node.next
        #two points to traversal 
        i, j=0, len(vec) - 1
        while i<j:
            vec[i].next = vec[j]
            i +=1
            if i == j:
                break
            vec[j].next = vec[i]
            j-=1
        vec[i].next = None
            