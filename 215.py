# -*- coding: utf-8 -*- 
'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
class Solution(object):
    def quicksort_once(self,nums,start,end):
        if start > end:
            return
        i = start
        j = end
        key = nums[start]
        while i < j:
            while nums[j] > key and i < j:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= key:
                i += 1
            nums[j] = nums[i]
        nums[i] = key
        return i
              
    def find(self,nums,start,end,k):
        if start > end:
            return
        temp = nums[start]
        index = self.quicksort_once(nums,start,end)
        if index == len(nums) - k:
            return temp
        elif index < len(nums) - k:
            start = index + 1
        else:
            end = index - 1
        return self.find(nums,start,end,k)
             
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < k or k < 1:
            return None
        begin = 0
        end = len(nums) - 1
        return self.find(nums,begin,end,k)
