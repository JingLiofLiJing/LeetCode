# -*- coding: utf-8 -*- 
'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        每个数建立一个字典，键为数字值，值为[出现次数，起始地址（在setdefault时已经指定）,最远末尾地址（每次更新）],然后再比较即可
        """
        dict = {}
        deg = 1
        minl = len(nums)
        for index,num in enumerate(nums):
            dict.setdefault(num,[0,index,index])
            dict[num][0] += 1
            if dict[num][0] > deg:
                deg = dict[num][0]
            if index > dict[num][2]:
                dict[num][2] = index
        for num in dict.keys():
            if dict[num][0] == deg:
                xxx = dict[num][2] - dict[num][1] + 1
                if xxx < minl:
                    minl = xxx
        return minl
