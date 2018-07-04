class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        number  = len(nums)
        for i in range(0,number):
            key = target - nums[i]
            if key in table:
                return [table[key],i]
            else:
                table[nums[i]] = i
        return  
        
