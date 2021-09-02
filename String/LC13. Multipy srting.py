def multiply(self, num1: str, num2: str) -> str:
        num1_len = len(num1)#把两个字符串的长度计算出来
        num2_len = len(num2)#把两个字符串长度计算出来
        res = [0] * (num1_len + num2_len)#现在的结果是 0
        for i in range(num1_len-1, -1, -1):
            for j in range(num2_len-1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + int(res[i+j+1])
                res[i+j+1] = tmp%10
                res[i+j] = res[i+j] + tmp//10
        res = list(map(str, res))
        for i in range(num1_len + num2_len):
            print(i)
            if res[i] != '0':
                return "".join(res[i:])
        return '0'