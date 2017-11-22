# -*- coding: utf-8 -*- 
'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        动态规划：设steps为达到对应楼梯高度可以选择的方案数，其中1（对应steps下标为0）为1，2为2，对于大于2的正整数n（下标为n-1），则方案为
        steps（n-1）（n-2的方案加1步）+steps（n-2）（n-3的方案加2步）即可
        """
        steps = []
        for i in range(1,n+1):
            if i == 1:
                steps.append(1)
            elif i == 2:
                steps.append(2)
            else:
                steps.append(steps[-1]+steps[-2])
        return steps[-1]
        
