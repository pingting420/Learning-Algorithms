#using two points
def judgeSquareSum(c):
    while low <= high:
        sumOf = low*low + high*high
        if sumOf == c: return True
        elif sumOf<c : low +=1
        else: high -=1
    return False
