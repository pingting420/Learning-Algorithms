def convertToTitle(n):
    s = ''
    while n>0:
        n = n-1
        c = n%26
        s = chr(65+c) + s
        n=n//26
    return s