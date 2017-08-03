# -*- coding: utf-8 -*-
'''
No.476
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = []
        first = False
        zs = 31
        res = 0
        #first为False表示还没有遇到第一个有效位，之前的0不做记录,也可以用bin（x）[2：]直接得到2进制串
        while zs >= 0:
            b = 2**zs
            cs = num/b
            if cs == 1:
                if first == False:
                    first = True
                a.append(1-cs)
                num = num - b
            elif cs == 0 and first == True:
                a.append(1-cs) 
            zs -= 1
        for i in range(len(a)):
            res += a[i]*(2**(len(a)-1-i))
        return res

print Solution().findComplement(5)