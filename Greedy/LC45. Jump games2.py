
        def jump(self, nums) -> int:
            if len(nums) == 1:return 0
            #record the numbers of jump
            ans = 0
            #cur the biggest distance
            curDistance = 0
            #the biggest distance
            nextDistance = 0
            #update the cover distance in the space
            for i in range(len(nums)):
                nextDistance = max(i + nums[i],nextDistance)
                if i == curDistance:
                    if curDistance != len(nums) - 1:
                        ans +=1
                        curDistance = nextDistance
                        if nextDistance >= len(nums) - 1:
                            return ans
                    