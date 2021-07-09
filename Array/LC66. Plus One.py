def plusOne(digits):
    num = int(''.join([str(s) for s in digits])) + 1
    return [int(s) for s in str(num)]

def plusone(digits):
    for i in range(1,len(digits) + 1):
        digits[-i] +=1
        if digits[-1] == 10:
            digits[-1] = 0
        else: break
        if digits[0]==0: digits = [1]+digits
        return digits