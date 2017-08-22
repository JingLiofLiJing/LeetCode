#-*- coding:utf-8 -*-
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #0到n的求和为0+1+...+n为（n+1）*n/2,把数组内的总元素加起来用总和减掉少的就是缺少的数字
        tot = ((len(nums)+1)*len(nums))/2
        res = 0
        for num in nums:
            res += num
        return tot - res

print Solution().missingNumber([0,2,3])