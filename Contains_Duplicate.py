#-*- coding:utf-8 -*-
'''
No.217
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #用字典遍历，值作为键，次数作为出现次数，次数大于等于2返回True，o（n）算法，排序为o（nlgn）
        dict = {}
        for num in nums:
            dict.setdefault(num,0)
            dict[num]+=1
            if dict[num] >= 2:
                return True
        return False