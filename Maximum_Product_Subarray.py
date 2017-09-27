# -*- coding: utf-8 -*-
'''
No.152
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        每个下标i对应的maxn和minn分别为以i下标为结尾的最大的数和最小的数。当i+1的时候，以i+1为结尾的最大或者最小的数要么是nums[i+1]本身，要么是i下标结尾的最大最小数乘上nums[i+1]的值，所以更新完i+1的maxn和minn的时候，再和总体的最大值比较更新r即为结果。
        """
        if nums == []:
            return 0
        maxn = minn = r = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0 :
                tmp = maxn
                maxn = minn
                minn = tmp
            maxn = max(maxn*nums[i],nums[i])
            minn = min(minn*nums[i],nums[i])
            r = max(r,maxn)
        return r
                
