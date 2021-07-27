def findKthPositive(self, arr, k) :
        left, right = 0, len(arr)-1

        while left <= right: # 左闭右闭的写法需要分析好你需要的值是left还是right
            mid = (left+right) // 2
            if k > arr[mid] - mid - 1:
                left = mid+1
            elif k <= arr[mid] - mid -1: 
                right = mid-1
        if right < 0:
            return arr[0] - (arr[0] - 0 - 1 - k) - 1 # arr[0] - (distance - k) - 1
        if k > arr[right] - right - 1:
            return arr[right] + k - (arr[right] - right - 1) # arr[right] + k - distance
