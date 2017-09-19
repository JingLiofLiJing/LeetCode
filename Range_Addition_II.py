# -*- coding: utf-8 -*- 
'''
No.598
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, 
which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after performing all the operations.
'''
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        对于每次操作，0 <= i < a and 0 <= j < b.的元素肯定都要受到影响，对于每次都影响左上角的元素，
        只要求出所有操作中的最小的共同影响的行数和列数再相乘即可
        """
        maxm = m
        maxn = n
        for i in range(len(ops)):
            a = ops[i][0]
            b = ops[i][1]
            if a<maxm:
                maxm = a
            if b<maxn:
                maxn = b
        return maxm*maxn
        
