def findRestaurant(list1, list2):
    l1, l2 = 0, 0
    k , v =[] ,[]
    for l1 in range(len(list1)):
        if list[l1] in list2:
            k.append(l1+list2.index(list1[l1]))
            v.append(list1[l1])
    min_val = min(k)
    return [v[i] for i in range(len(k)) if k[i]==min_val]