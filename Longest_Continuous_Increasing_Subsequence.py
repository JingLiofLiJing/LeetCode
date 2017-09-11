#-*- coding:utf-8 -*-
'''
No.674
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
'''
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        如果为空返回0，否则从第一个开始，默认最长为1本身，如果比前一个长则+1并向下迭代，并记录最大值即可
        """
        if nums == []:
            return 0
        i = 1
        max = 1
        while i < len(nums):
            tmp = 1
            while i < len(nums) and nums[i] > nums[i-1]:
                i += 1
                tmp += 1
            if tmp > max:
                max = tmp
            i += 1
        return max
            
