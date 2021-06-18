#split function
def countSegments(s):
    strs = s.split( )
    for i in strs:
        if i != "":
            return len(strs)



#return len([i for i in s.split(" ") if i !=""])

s = "Hello, my name is Pingting"
print(countSegments(s))