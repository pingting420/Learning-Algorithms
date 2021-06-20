#solution hash table:
#use the way of key and word, to check if there is any conflict
def wordPattern(pattern, s):
    word2ch = dict()
    ch2word = dict()
    words = s.split(s)
    if len(pattern) != len(words):
        return False
    # we can use the function of zip to realize the map relastionship
    for ch, word in zip(pattern, words):
        if (word in word2ch and word2ch[word] !=ch) or (ch in ch2word and ch2word[ch] != word):
            return False
        word2ch[word] = ch
        ch2word[ch] = word
    return True