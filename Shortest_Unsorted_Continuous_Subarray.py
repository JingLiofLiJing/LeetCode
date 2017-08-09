# -*- coding: utf-8 -*- 
'''
No.581
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.
'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #首先找出第一个比右边大（从左到右）的下标i和第一个比左边小（从右到左）的下标j，则[i,j](i到j闭区间)为基本的转换区间，然后求出区间的最小值和最大值，对于i，找到第一个小于等于最小值的index，对于j找到第一个大于等于最大值的index
        #即为所求的最小区间[i+1,j-1]闭区间，长度为j-i-1。除此之外，如果序列原本正确，则i和j一样，长度值小于0单独处理即可
        if len(nums) <= 1:
            return 0
        i = 0
        j = len(nums)-1
        while i + 1 < len(nums) and nums[i] <= nums[i+1]:
            i += 1
        while j - 1 >=0 and nums[j] >= nums[j-1]:
            j -= 1
        small = nums[i]
        large = nums[i]
        k = i+1
        while k <= j:
            if nums[k] < small:
                small = nums[k]
            if nums[k] > large:
                large = nums[k]
            k += 1
        while i >= 0 and nums[i] > small:
            i -= 1
        while j < len(nums) and nums[j] < large:
            j += 1
        res = j - i - 1 
        if res < 0 :
            res = 0
        return res
print Solution().findUnsortedSubarray([1]) 

