# -*- coding: utf-8 -*- 
'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #首先判断整数，然后如果可以一直整除2或3或5到1则返回true，其他返回false
        if num <= 0:
            return False
        while True:
            if num == 1:
                return True
            if num % 2 == 0:
                num = num/2
            elif num % 3 == 0:
                num = num/3
            elif num % 5 == 0:
                num = num/5
            else:
                return False
        
