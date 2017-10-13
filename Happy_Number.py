# -*- coding: utf-8 -*-
'''
No.202
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this 
process ends in 1 are happy numbers.
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        #每一位平方和相加，结果一直迭代，只要有结果为1的则为答案，所以每次循环只要判断是否为1即可
        """
        if n <= 0:
            return False
        ws = []
        while True:
            sum = 0
            while n!=0:
                a = n%10
                sum += a*a
                n = (n - a)/10
            if sum == 1:
                return True
            elif sum in ws:
                return False
            ws.append(sum)
            n = sum
