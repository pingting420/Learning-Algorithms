from collections import deque
d = deque()
d.append(2)
d.append(3)
d.append(8)
print(d)

a = deque('12345')
a.pop()
print(a)
a.leftpop()
print(a)