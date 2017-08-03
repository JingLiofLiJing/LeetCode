# -*- coding: utf-8 -*-
'''
Write a function that takes an unsigned integer and returns the number of ��1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ��11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = 31
        res = 0
        while index >= 0:
            dishu = 2**index
            a1 = n / dishu
            if a1 == 1:
                res += 1
            index -= 1
            n = n - a1*dishu
        return res