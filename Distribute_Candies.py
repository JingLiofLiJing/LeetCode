# -*- coding: utf-8 -*- 
'''
No.575
Given an integer array with even length, where different numbers in this array represent different kinds of candies. 
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. 
Return the maximum number of kinds of candies the sister could gain.
'''
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #字典存储时间复杂度为O（1）
        dict = {}
        for candy in candies:
            dict.setdefault(candy,0)
            dict[candy]+=1
        a = len(dict.keys())
        b = len(candies)/2
        #如果每个人拥有的数量小于总的种类，则返回n，否则返回已有的种类即可
        if b<=a:
            return b
        else:
            return a