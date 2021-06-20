def Keyboard(words):
    set1 = ('qwertyuiop')
    set2 = ('asdfghjkl')
    set3 = ('zxcvbnm')
    res = []
    for i in words:
        x = i.lower()
        setx = set(x)
        if setx <= set1 or setx <= set2 or setx <= set3:
            res.append(i)
    return res


