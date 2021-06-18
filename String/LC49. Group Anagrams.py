#Has two solutions
#One solution using sort, and the other using hash table


#List after join will become string
#result.values() will feed the values directly
def groupAnagrams(str):
    if len(str) < 2:
        return [str]
    result = {}
    for i in str:
        temp = ''.join(sorted(i))
        #sort each string, and combine the sorted list into a string
        #sotred("cba")->['a','b','c']
        #"".join(sorted('cba'))->'abc'

        result[temp]= result.get(temp,[])+[i]
        #dict.get(x,y),x is the key, y is the default value
        #if dict doesn't have the key x, it will return y as the value
        #if dict has the key x, it will return the actual value of x
    return result.values()

    #Solution2 Hash Table
def groupAnagrams2(str):
    if len(str) <2:
        return [str]
    result = {}
    for i in str:
        count_table =[ord(i) - ord('a')]+=1
        #list can not be hash, but the key of dict has to be hashable
        #so we have to change list to tuple
        key = tuple(count_table)
        result[key] = result.get(key,[])+[i]
    return result.values()



