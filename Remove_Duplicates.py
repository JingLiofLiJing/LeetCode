# -*- coding: utf-8 -*- 
'''
No.80
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    def swap(self,nums,i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        #目标：移动数组元素，不破坏数组的内容。设置i表示满足要求的数字的总数，j遍历数组，duplic为最新的i下标处的数字的重复次数
        #由于可能存在多次重复，所以j会比i大，从0到i-1的数字都是符合要求的排列，当j数字和i-1数字一样时，如果重复次数超过1，则j加
        #1，i不更新；否则将j和i的数字对换。如果j和i-1不一样，则i也更新，同时dplic变为1，表示当前数字第一次出现。
        """
        i = 0
        j = 0
        duplic = 0
        while j < len(nums):
            if i == 0:
                i += 1
                duplic += 1
            elif nums[j] == nums[i - 1]:
                if duplic <= 1:
                    duplic += 1
                    self.swap(nums,i,j)
                    i += 1
            else:
                self.swap(nums,i,j)
                i += 1
                duplic = 1
            j += 1
        return i
        
        
