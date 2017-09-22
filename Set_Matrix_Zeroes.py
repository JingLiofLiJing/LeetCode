# -*- coding: utf-8 -*-
'''
No.73
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        采用固定额外空间l和d分别表示第0行和第0列是否要全0，先遍历数组，如果存在0，则将该列的第一个数和改行的第一个数打上“x”标记
        如果在第一列，则d=1，第一行则l=1；之后从下标1开始遍历第一列和第一行，如果为x则整行整列都为0，最后再根据ld的值把第一列和
        第一行为0.
        """
        l = d = 0
        if matrix != [] and len(matrix[0]) != 0:
            m = len(matrix)
            n = len(matrix[0])
            for i in range(0,m):
                for j in range(0,n):
                    if matrix[i][j] == 0:
                        if i == 0:
                            l = 1
                        if j == 0:
                            d = 1
                        matrix[0][j] = matrix[i][0] = 'x'
            for i in range(1,m):
                if matrix[i][0] == 'x':
                    for j in range(0,n):
                        matrix[i][j] = 0
            for j in range(1,n):
                if matrix[0][j] == 'x':
                    for i in range(0,m):
                        matrix[i][j] = 0
            if l == 1:
                for j in range(0,n):
                    matrix[0][j] = 0 
            if d == 1:
                for j in range(0,m):
                    matrix[j][0] = 0      
        return matrix     
            
print Solution().setZeroes([[1,2,3,4],[5,0,5,2],[8,9,2,0],[5,7,2,1]])
