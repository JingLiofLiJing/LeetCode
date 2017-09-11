# -*- coding: utf-8 -*-
'''
No.258
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        #第一层循环当结果不为单个整数时继续执行，第二层循环计算每位数字的和在进行判断
        """
        no = num
        while no >= 10:
            tmp = 0
            while no >= 10:
                a = no%10
                tmp += a
                no = (no - a)/10
            no = tmp + no
        return no
        
    def o1(self, num):
        """
        :type num: int
        :rtype: int
        #o（1）解法：数学知识
        0      0
        1-9    1-9
        10-18  1-9
        19-27  1-9
        27-36  1-9
        ....
        当数字能被9整除但不为0时则返回9，其余返回9的余数，shit。
        """
        if num!=0 and num%9 == 0:
            return 9
        else:
            return num%9
            
                
        
