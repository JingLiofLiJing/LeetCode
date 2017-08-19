#-*- coding:utf-8 -*-
'''
No.283
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #i用来记录非0的下标，j遍历数组，遇到不为0的数字和i处数字互换，则最后所有的0元素都被换到后方
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
            j += 1
        return nums


