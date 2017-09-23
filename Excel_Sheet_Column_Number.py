# -*- coding: utf-8 -*-
'''
No.171
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        实际上是一个26进制数
        """
        res = 0
        base = 1
        for i in range(len(s)-1,-1,-1):
            res += (ord(s[i].upper())-ord('A')+1) * base
            base *= 26
        return res
        
