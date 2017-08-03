# -*- coding: utf-8 -*-
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

0 ≤ x, y < 2**31
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #按位比较就行
        index = 30
        res = 0
        while index >= 0:
            dishu = 2**index
            a1 = x / dishu
            a2 = y / dishu
            if a1 != a2:
                res += 1
            index -= 1
            x = x - a1*dishu
            y = y - a2*dishu
        return res

print Solution().hammingDistance(1, 4)
        