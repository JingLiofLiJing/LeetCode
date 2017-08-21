#-*- coding:utf-8 -*-
'''
No.218
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #存在相邻的两个数，这两个数的下标差值小于等于k即可，用字典记录前一个下标，每次遇到相同的数字比较和之前下标的差是否满足要求后再覆盖前一个下标即可
        #复杂度o（n）
        dict = {}
        for index,num in enumerate(nums):
            dict.setdefault(num,index)
            if dict[num] != index and index - dict[num] <= k :
                return True
            dict[num] = index
        return False