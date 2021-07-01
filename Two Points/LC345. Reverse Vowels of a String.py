def reverseVowels(s):
    dic = {'a','e','i','o','u','A','E','I','O','U'}
    lst = list(s)
    n = len(s)
    l ,r = 0, n-1
    while l < r:
        if lst[l] in dic and lst[r] in dic:
            lst[l], lst[r] = lst[r], lst[l]
            l +=1
            r -=1
        elif lst[l] not in dic:
            l +=1
        elif lst[r] not in dic:
            r -=1
    return ''.join(lst)