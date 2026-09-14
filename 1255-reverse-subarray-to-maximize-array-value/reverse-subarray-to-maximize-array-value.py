class Solution(object):
    def maxValueAfterReverse(self, nums):
        n = len(nums)
        
        # Step 1: base value
        base = 0
        for i in range(n-1):
            base += abs(nums[i] - nums[i+1])
        
        # Step 2: check boundary improvements
        gain = 0
        
        # Case 1: reverse subarray touching left boundary
        for i in range(1, n-1):
            gain = max(gain, abs(nums[0] - nums[i+1]) - abs(nums[i] - nums[i+1]))
        
        # Case 2: reverse subarray touching right boundary
        for i in range(1, n-1):
            gain = max(gain, abs(nums[n-1] - nums[i-1]) - abs(nums[i] - nums[i-1]))
        
        # Case 3: reverse middle subarray
        min2 = float('inf')
        max2 = -float('inf')
        for i in range(n-1):
            a, b = nums[i], nums[i+1]
            min2 = min(min2, max(a, b))
            max2 = max(max2, min(a, b))
        gain = max(gain, (max2 - min2) * 2)
        
        return base + gain
