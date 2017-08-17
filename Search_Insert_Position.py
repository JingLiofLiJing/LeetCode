# -*- coding:utf-8 -*-
'''
No.35
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''
class Solution(object):
    def searchInsert_normal(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #判断开头和结尾位置
        if nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        #判断中间位置
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if  i + 1 < len(nums) and nums[i] < target and nums[i+1] > target:
                return i+1
            i += 1

        #2分法进行查找效率高
        def search_bs(self,nums,target):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end)/2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
            return start