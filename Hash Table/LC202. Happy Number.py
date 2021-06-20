# This problem we should use hashtable, this data structure will use time cpmliexity of O(1) but not O(N) like other data structure
#Solution1 : use set
# While loop , the n != 1
#If n already in the loop, then false 
#There are two situation: happy number or loop never end
def isHappy(n):
    def get_next(n):#function to get the next num
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum
    
    seen = set()
    while n!= 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n==1
#Time Complexity:O(logN)


#Solution two points: slow and fast two point to check if there is a circule in the list
#put the res in a list: use slow and fast
# if slow not equal to fast , slow 
#if slow equal to fast, slow ==1 equal to happy num
#function: getNext(n)


def isHappy2(n):
    def get_next(n):
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit **2
    return total_sum

slow_runner = n
fast_runner = get_next(n)
#fast is the first to =1
while fast_runner != 1 and slow_runner != fast_runner:
    #The speed of fast is two times faster than slower
    slow_runner = get_next(slow_runner)
    fast_runner = get_next(get_next(fast_runner))
return fast_runner == 1
#Time complexity : O(logN)



