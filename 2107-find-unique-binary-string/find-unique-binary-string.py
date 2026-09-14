class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            # flip the i-th character of nums[i]
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return "".join(result)

        