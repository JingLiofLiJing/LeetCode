# -*- coding: utf-8 -*- 

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        dict哈希，时间复杂度低
        """
        dict = {}
        for index,num in enumerate(nums):
            dict[num] = index                    #哈希表加快速度
        for id,num in enumerate(nums):
            if target - num in nums:
                if dict[target-num] != id:
                    return[id,dict[target-num]]
nums = [-3,4,3,30]
target = 0
test = Solution()
print test.twoSum(nums, target)