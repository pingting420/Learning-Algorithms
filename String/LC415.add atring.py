def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry #n1 + n2 + 进位
            carry = tmp // 10 #进位是除以10的倍数，carry保存的是进位，在下一次计算时候会加上去
            res = str(tmp % 10) + res #结果是加上除以10的余数 #这个不是加法，而是直接加在后面
            i, j = i - 1, j - 1
        return "1" + res if carry else res