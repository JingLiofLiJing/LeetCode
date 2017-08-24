# -*- coding: utf-8 -*-
'''
No.121
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
'''
class Solution(object):  
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #动态规划算法：每一次遍历的best保存的为最大的符合要求的差值，同时mmin保存从下标0到所遍历下标处的范围内的最小值。
        if len(prices) <= 1:
            return 0
        best = 0
        mmin = prices[0]
        for i in range(1,len(prices)):
            if best < prices[i] - mmin:
                best = prices[i] - mmin
            if prices[i] < mmin:
                mmin = prices[i]
        return best
      
