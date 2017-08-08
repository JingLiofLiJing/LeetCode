# -*- coding: utf-8 -*- 
'''
No.26
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #一开始i=0，j为下一位，找到下一个大的j并与i+1交换，变化成i+1，j一直往下，如果找不到说明i为最大，返回i+1即为个数（list下标从0开始）
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums) and nums[j] <= nums[i]:
                j += 1
            if j == len(nums):
                return i+1
            if j < len(nums):
                temp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = temp
            i = i + 1

print Solution().removeDuplicates([1,1,2,2,3,3,4,4,4,5,6,7,7])