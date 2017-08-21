#-*- coding:utf-8 -*-
'''
No.661
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray
scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
'''
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        #判断周围的点即可
        #col：行   row：列
        col = len(M)
        row = len(M[0])
        resutl = []
        for i in range(col):
            temp = []
            for j in range(row):
                xx = [M[i][j],1]
                #上三个数（i-1.j-1）（i-1,j）（i-1,j+1）
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        xx[0] += M[i-1][j-1]
                        xx[1] += 1
                    if j + 1 < row:
                        xx[0] += M[i-1][j+1]
                        xx[1] += 1
                    xx[0] += M[i-1][j]
                    xx[1] += 1
                # 下三个数（i+1.j-1）（i+1,j）（i+1,j+1）
                if i + 1 < col:
                    if j - 1 >= 0:
                        xx[0] += M[i+1][j-1]
                        xx[1] += 1
                    if j + 1 < row:
                        xx[0] += M[i+1][j+1]
                        xx[1] += 1
                    xx[0] += M[i+1][j]
                    xx[1] += 1
                #左边（i,j-1）
                if j - 1 >= 0:
                    xx[0] += M[i][j-1]
                    xx[1] += 1
                # 右边（i,j+1）
                if j + 1 < row:
                    xx[0] += M[i ][j + 1]
                    xx[1] += 1
                temp.append(xx[0]/xx[1])
            resutl.append(temp)
        return resutl
print Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])