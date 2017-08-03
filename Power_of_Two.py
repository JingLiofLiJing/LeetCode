# -*- coding: utf-8 -*-
'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        index = 31
        while index >= 1:
            dishu = 2**index
            a1 = n / dishu
            n = n - a1 * dishu
            if a1 == 1:
                #减了2的次方还有余数则不满足条件
                if n == 0:
                    return True
                else:
                    return False
            index -= 1
        if n == 0:
            return False
        return True