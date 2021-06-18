def lengthLastWord(s):
    s = s.strip(" ")
    l = s.split(" ")[-1]
    return len(l)
#two function 
#one strip, this function can delete the blank in the head and last
#split can split the str using specific symbol

s = lengthLastWord(" Hello World")
print(s)