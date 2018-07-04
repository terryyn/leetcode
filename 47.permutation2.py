#Given a collection of numbers that might contain duplicates, return all possible unique permutations.

def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]
    result = []
    index = 0
    visited = []
    for index in range(len(nums)):
        temp = [nums[index]]
        if index > 0 and nums[index] in visited:
            continue
        temp_result = self.permuteUnique(nums[:index]+nums[index+1:])
        for part in temp_result:
            tp = temp+part
            result.append(tp)
        visited.append(nums[index])
    return result
    
    
 #exactly the same as 
