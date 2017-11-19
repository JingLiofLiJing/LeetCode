# -*- coding: utf-8 -*- 
'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
'''
# -*- coding: utf-8 -*- 
class Solution(object):

    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        #动态规划算法，建立一个lenA*lenB的矩阵，其中每一个元素（i,j）表示以A的第i个元素结尾和B的第j个元素结尾的相同子字符串的最长长度，
        先初始化第一行和第一列，因为是A的第一个或者B的第一个，所以如果匹配的话为1，然后中间的如果匹配的话，值为i-1，j-1结尾字符串的长度
        加上1
        """
        maxd = 0
        lenA = len(A) 
        lenB = len(B)
        mat = [[0]*lenB for i in range(lenA)]
        for i in range(lenA):
            if A[i] == B[0]:
                mat[i][0] = 1
        for i in range(lenB):
            if A[0] == B[i]:
                mat[0][i] = 1
        for i in range(1,lenA):
            for j in range(1,lenB):
                if A[i] == B[j]:
                    mat[i][j] = 1 + mat[i-1][j-1]
                    maxd = max(mat[i][j],maxd)
        return maxd
        
    
print(Solution().findLength([0,0,0],[0,0,0,0]))
