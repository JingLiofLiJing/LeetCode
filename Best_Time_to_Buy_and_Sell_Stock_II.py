#-*- coding:utf-8 -*-
'''
No.122
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #找出每一段上升区间的两端相减即可,o(n)算法
        i = 0
        res = 0
        #找到第一个最小点
        while i+1 < len(prices) and prices[i+1] <= prices[i]:
            i += 1
        while i < len(prices) - 1:
            xiao = prices[i]
            while i + 1<len(prices) and prices[i+1] >= prices[i]:
                i+= 1
            da = prices[i]
            res += da - xiao
            while i + 1 < len(prices) and prices[i + 1] <= prices[i]:
                i += 1
        return res
print Solution().maxProfit([10,10,20,10,10])

