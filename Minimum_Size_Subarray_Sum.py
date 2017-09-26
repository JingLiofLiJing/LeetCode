# -*- coding: utf-8 -*- 
'''
No.209
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.For example, given the array [2,3,1,2,4,3] and s = 7,the subarray [4,3] has the minimal length 
under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        垃圾解法:分别以每一个下标为开头寻找第一个大于s的序列并比较长度，知道加到最后一个数后仍然小于s则结束
        o（n）解法
        """
        if len(nums) == 0:
            return 0
        i = j = tmp = 0
        res = -1
        while i < len(nums):
            while j < len(nums):
                tmp += nums[j]
                if tmp >= s:
                    if res == -1:
                        res = j-i+1
                    elif j-i+1 <res:
                        res = j-i+1
                    break
                j += 1
            #结束条件：剩下的序列总和仍小于s
            if j == len(nums):
                break
            #将i向后移动一位，所以减掉i的值同时减掉j的值防止重复计算
            tmp = tmp - nums[i] - nums[j]           
            i+=1
        if res == -1:
            return 0
        return res
                
