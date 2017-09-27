# -*- coding: utf-8 -*-
'''
No.153
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
'''
class Solution(object):
    def haha(self,nums,start,end):
        if start == end:
            return nums[start]
        mid = (end+start)/2
        #不写成a = self.haha(nums,start,mid-1)和b = self.haha(nums,mid+1,end)的原因是如果start+1=end的话
        #mid-1会小于start，则逻辑错误。
        a = self.haha(nums,start,mid)
        b = self.haha(nums,mid+1,end)
        return min(a,b)
        
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2分法查找即可，o（logn）
        """
        return self.haha(nums,0,len(nums)-1)
        
