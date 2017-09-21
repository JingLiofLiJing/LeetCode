# -*- coding: utf-8 -*-
'''
No.75
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.
'''
class Solution(object):
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        同时放置好0和2的顺序，按题目来说0在最左边，2在最右边，则j为排好0的i下一个序号，k为排好2的下一个序号，i进行遍历，如果nums[i]为0，则
        将此处的值与j处数字对换，j+1表示又排好了一个0的数字，同理如果nums[i]为2，则将此处的值与k处数字对换，k-1表示又排好了一个2的数字，只
        需要遍历到i等于k就行了，因为后面都是已经排好的2，自然j,k中间都是1，时间复杂度on，空间复杂度o1.
        """
        j = 0
        k = len(nums) - 1
        i = 0
        while i <= k:
            if nums[i] == 0:
                self.swap(nums,i,j)
                j += 1
            elif nums[i] == 2:
                self.swap(nums,i,k)
                k -= 1
                i -= 1
            i += 1
            
            
            
print Solution().sortColors([0,2,2,2,1,1,1,0,0,1,2,2,1])
