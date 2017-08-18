# -*- coding:utf-8 -*-
'''
No.643
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value.
And you need to output the maximum average value.
'''
class Solution(object):
    def findMaxAverage_baoli(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #暴力求解，o（n**2）
        i = 0
        max = -10000
        while i <= len(nums) - k :
            xx = 0
            j = 0
            res = 0
            while j < k:
                xx += nums[i+j]
                j += 1
            res = float(xx)/k
            if res > max:
                max = res
            i += 1
        return max

    def findMaxAverage(self, nums, k):
        #求最大平均值，可以先求出最大的总和
        #将max的值设置为第一组前k个数的和，后面的依次减去最小的下标值再加上下一个下标值求和依次到最后一组，并不断更新最大总和即可o（n）算法
        i = 0
        j = k - 1
        max = temp = 0
        while i <= j:
            max += nums[i]
            i += 1
        temp = max
        i = 0
        j += 1
        while j  < len(nums):
            temp = temp - nums[i] + nums[j]
            i += 1
            j += 1
            if temp > max:
                max = temp
        return float(max)/k

print Solution().findMaxAverage([1,12,-5,-6,50,3],4)
