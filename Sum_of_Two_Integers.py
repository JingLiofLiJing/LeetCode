# -*- coding: utf-8 -*- 
'''
No.371
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        #采用伪加法，a^b代表除了进位之外的和的表示，然后a&b代表每一位得到的进位值，然后进位值向左移动一位再和之前的部分和表示相加得到新的和，以此不断
        #更新a和b知道b为0，a即为加法的结果。
        #由于python中整数不是固定的32位，所以需要做一些特殊的处理。 代码里一个数对0x100000000取模（注意：Python的取模运算结果恒为非负数），是希望该
        数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），以在0-31位上模拟一个32位的int。
        """
        while b!= 0:
            carry = (a&b) << 1
            a = (a^b) % 0x100000000
            b = carry % 0x100000000
        #考虑到和超过32位的情况
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
        
        
