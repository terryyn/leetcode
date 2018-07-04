"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

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
  
 
#a simple hash table algorithm, here I use one-pass but two-pass is also ok
