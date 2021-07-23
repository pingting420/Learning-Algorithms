def findPeakElement(nums):
        if len(nums) == 1: return 0
        n = len(nums)
        if nums[0]>nums[1]:return 0
        if nums[n-1] > nums[n-2]:return n-1
        
        left, right = 0,n-1
        #left<=mid <right<n, 因此nums[mid+1]不出界
        while left < right:
            mid = (left+right)//2
            if nums[mid]<nums[mid+1]:#说明mid在递增段
                left = mid+1
            elif nums[mid]>nums[mid+1]:#说明mid在递减段
                right = mid
            elif nums[mid] == nums[mid+1]:#无法判断向左撤退缩小范围
                old_mid = mid
                while mid>left and nums[mid] == nums[mid+1]:
                    mid-=1
                #如果退回到原点，则nums[left]=...nums[old_mid]在峰的另一侧
                if mid==0 : left = old_mid+1
                if nums[mid]<nums[mid+1]:
                    left = mid+1
                else:
                    right = mid
        return left