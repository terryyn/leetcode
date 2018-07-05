class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0]*(len(nums))
        index = 1
        result = nums[0]
        dp[0] = nums[0]
        while index < len(nums):
            if dp[index-1] < 0 :
                dp[index] = nums[index]
            else:
                dp[index] = dp[index-1]+nums[index]
            if result < dp[index]:
                result = dp[index]
            index+=1
        return result
