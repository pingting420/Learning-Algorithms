#Solution1: divide the string into list, and reverse every word.
def reverseWords(s):
    return" ".join(word[::-1] for word in s.split(" "))

#Solution2: 
def reverseWords(s):
    return " ".join(s.split(" ")[::-1][::-1])


#solution3:
def reverseWords(s):
    #'I love drag queen'
    s[::-1]#reverse string
    #neeuq gard evol I
    s[::-1].split(" ")#devide to word list
    #'neeuq', 'grad', 'evol', 'I
    #reverse the word list
    s[::-1].split(" ")[::-1]
    #transform to the string with join
    " ".join(s[::-1].split(" ")[::-1])


