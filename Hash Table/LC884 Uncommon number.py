def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = []
        s3 = s1.split(" ") + s2.split(" ")
        for i in s3:
            if s3.count(i) == 1:
                table.append(i)
        return table