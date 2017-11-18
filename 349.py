
# -*- coding: utf-8 -*- 
'''
Given two arrays, write a function to compute their intersection.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #求集合交集即可
        return list(set(nums1) & set(nums2))
