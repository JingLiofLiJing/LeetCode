# -*- coding: utf-8 -*- 
'''
No.566
Given an integer array with even length, where different numbers in this array represent different kinds of candies. 
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. 
Return the maximum number of kinds of candies the sister could gain.
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ro = len(nums)
        co = len(nums[0])
        #行列不符合要求返回原来数组
        if ro*co != r*c:
            return nums
        res = []
        i = 0
        jj = []
        while i < ro:
            #从头开始
            j = 0
            while j < co:
                jj.append(nums[i][j])
                if len(jj) == c:
                    res.append(jj)
                    jj = []
                j += 1
            i += 1
        return res