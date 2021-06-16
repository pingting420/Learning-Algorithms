# If we want to find the index in a str, we should using hash.
#enumerate can feed the num and index
from collections import Counter
def firstuniqChar(s):
    frequency = collections.Counter(s)
    for i, ch in enumerate(s):
        if frequency[ch] == 1:
            return i
    return -1


# using get function


def firstuniqChar(s):
    c = Counter(s)
    for i in s:
        #C[i] is the number of Counter
        if c[i] == 1:
            return s.index(i)
    return -1