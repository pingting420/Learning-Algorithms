def roman(s):
    dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    #define a num as the first num
    num = dict[s[0]]

    for i in range(1,len(s)):
        #situation 1: if previous numeral is lesser than the one currently, it means we have to subtract
        if dict[s[i-1]] < dict[s[i]]:

        #clean the num
           num = num - dict[s[i-1]]
        #substract the current and previous pointer and add it value to the num
           num = num + dict[s[i]] - dict[s[i-1]]
        else:
            num = num + dict[s[i]]
    return num
