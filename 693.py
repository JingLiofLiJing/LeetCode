# -*- coding: utf-8 -*- 
'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst = bin(n)[2:]
        if len(lst) > 1:
            for i in range(1,len(lst)):
                if lst[i] == lst[i-1]:
                    return False
        return True
        
        
