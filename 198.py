# -*- coding: utf-8 -*- 
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        max2为最多以此处为结尾的前面的所有符合要求的序列的最大，max1为必须以此处为结尾的最大子串的距离，则没到下一个地方依次更新max2和max1，同时此处的最        大值为max1，再与maxd比较即可
        """
        if nums == []:
            return 0
        if len(nums) < 3:
            return max(nums)
        max2 = nums[0]
        max1 = nums[1]
        maxd = max(max1,max2)
        for i in range(2,len(nums)):
            temp = max1
            max1 = max(max2+nums[i],max1)
            max2 = max(temp,max2)
            maxd = max(max1,maxd)
        return maxd
        
    
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划方法，nums[i]表示i下标以及之前最大的子序列和，所以i下标表示i-2之前和i以及i-1的最大值，分别表示不选i和选i。
        是上个方法的简化版
        """
        if nums == []:
            return 0
        if len(nums) < 3:
            return max(nums)
        nums[1]=max(nums[:2])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        return nums[-1]
