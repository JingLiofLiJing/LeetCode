# -*- coding: utf-8 -*- 
'''
No.55
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        每一次从后往前找到第一个可以跳到的点，如果能匹配到第0个点，说明可达，否则不可达，
        o（n）时间复杂度
        """
        if len(nums) <= 1:
            return True
        i = len(nums) - 2
        target = len(nums) - 1
        ys = False
        while i >= 0 :
            if nums[i] < target - i:
                i -= 1
                continue
            if i == 0:
                ys = True
                break
            target = i
            i -= 1
        return ys
    
    #贪心算法：每次找到能够达到的最远距离，如果下一个下标能够到更远的距离则更新最远距离，如果最后一个下标也在可达范围内则True，
    如果下标超过可达范围则不可达。   
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
