def longestCommonPrefix(strs):
    if not strs:
        return ""
    length = len(strs[0])#define the length of the first string, and use length to store the length
    for i in range(len(strs)):#travelsal all of the strs in strs
        length = min(length, len(strs[i]))#give the min length to the length
        if length == 0:
            return ""
        for j in range(length):#travelsal and compare the first str and the current str, if there any difference, bresk
           if strs[0][j] != strs[i][j]:
               length = j#give the length to the length
               break
    return strs[0][:length] 

