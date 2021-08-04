def numRabbits(self, answers):
        count = Counter(answers)
        ans = sum((x+y)//(y+1)*(y+1) for y, x in count.items())
        return ans
        