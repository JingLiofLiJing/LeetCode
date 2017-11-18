# -*- coding: utf-8 -*- 
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #和最小代价计算一样，只不过一开始第一列和第一行的格子为1，代表从左上角到此格子有多少种走法，最后一直累加到右下角即可
        a = []
        for i in range(m):
            les = [1]
            for j in range(n-1):
                if i == 0:
                    les.append(1)
                else:
                    les.append(0)
            a.append(les)
        for i in range(1,m):
            for j in range(1,n):
                a[i][j] = a[i][j-1]+a[i-1][j]
        return a[-1][-1]
