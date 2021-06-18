#this exercise should compare with the 557
#shold compare the reversed and [::-1]
#We should notice that the string counldn't change
def reverseWrds(s):
    return " ".join(reversed(s.split()))

#solution 2
#We can trim the spaces and convert string into array
#reversed the array
#reverse each word
#join
def trim_spaces(s):
    left, right = 0, len(s)-1
    while left <= right and s[left] ==" ":
        left += 1

while left <= right and s[right] ==" ":
    right -= 1

output = []
while left <= right:
    if s[left] != ' ':
        output.append(s[left])
    elif output[-1] != ' ':
        output.append(s[left])
    left += 1
return output

def reverse(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left, right = left+1, right -1

def reverse_each_word(l):
    n = len(l)
    start = end = 0

    while start < n:
        while end<n and l[end] != ' ':
            end+=1
        self.reverse(l,start,end-1)
        start = end+1
        end+=1

def reverseWords(s):
    l = self.trim_spaces(s)

    self.reverse(1,0,len(l)-1)
    self.reverse_each_word(l)
    return ''.join(l)

