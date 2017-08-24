# -*- coding:utf-8 -*-
'''
Given a binary array, find the maximum number of consecutive 1s in this array.
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #遍历即可
        best = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
                continue
            tmp = 0
            while i < len(nums) and nums[i] == 1:
                tmp += 1
                i+= 1
            if best < tmp:
                best = tmp
        return best
            
