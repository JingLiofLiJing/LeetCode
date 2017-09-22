#coding=utf-8
'''
No.48
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        #先让矩阵转置，然后再左右对换即可完成顺时针旋转90度，题目其实是转置的镜像
        """
        ln = len(matrix)
        if ln > 0:
            for i in range(ln):
                for j in range(0,i):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            i = 0
            j = ln - 1
            while i < j:
                for m in range(0,ln):
                    temp = matrix[m][i]
                    matrix[m][i] = matrix[m][j]
                    matrix[m][j] = temp
                i += 1
                j -= 1
            
