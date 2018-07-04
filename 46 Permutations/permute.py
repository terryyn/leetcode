class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []
        index = 0
        for index in range(len(nums)):
            temp = [nums[index]]
            temp_result = self.permute(nums[:index]+nums[index+1:])
            for part in temp_result:
                tp = temp+part
                result.append(tp)
        return result
