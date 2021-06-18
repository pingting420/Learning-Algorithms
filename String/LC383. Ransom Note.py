def canConstruct(ransomNote, magazine):
    #if want to find some difference between, it's important to use set function
    letter = set(ransomNote)
    for i in letter:
        if magazine.count(i) <ransomNote.count(i):
            return False
    return True
#conclusion: set, collections.Counter, split(), enumerate


#sloution2 hash map
def canConstruct(ransomNote, magazine):
    ransomNote = r
    magazine = m
    freq_r = Counter(r)
    freq_m = Counter(m)
    for i in freq_r:
        if freq_r[a]>freq_m[a]:
            return False
    return True