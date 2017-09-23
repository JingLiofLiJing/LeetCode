
# -*- coding: utf-8 -*-
'''
No.168
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        实际上是一个26进制数转字母串,但是余数为0对应的是26的Z，所以单独判断一下
        """
        list = []
        while n > 0 :
            ys = n % 26
            if ys == 0:
                list.append('Z')
                n -= 26
            else:
                list.append(chr(ys+64))
                n -= ys
            n /= 26
        list.reverse()
        return ''.join(list)
        
