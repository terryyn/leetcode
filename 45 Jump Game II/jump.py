class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        result = 0
        while index < len(nums)-1:
            result +=1 
            if nums[index]+index >= len(nums)-1:
                return result
            temp = index+1
            destination = 0
            cur = 0 + nums[index]
            
            #instead of choosing the index with biggest capacity in the range
            #choose the index which can reach farthest from the starting index
            
            while temp <= index+nums[index]:
                if nums[temp]+temp-index>=cur:
                    destination = temp
                    cur = nums[temp]+temp-index
                temp+=1
            index = destination
        return result
