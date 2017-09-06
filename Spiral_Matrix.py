# -*- coding: utf-8 -*- 
'''
No.54
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if matrix == []:
            cols = 0
        else:
            cols = len(matrix[0])
        #one tow遍历行
        one = 0
        two = rows - 1
        #three four 遍历列
        three = 0
        four = cols - 1
        res = []
        #one,two,three,four分别控制环状访问的边界，每次遍历完一圈向内更新
        while one <= two and three <= four:
            i = one
            for j in range(three,four):
                res.append(matrix[i][j])
            j = four
            for i in range(one,two):
                res.append(matrix[i][j])
            i = two
            #防止one two 或者 three four相等额外添加重复元素，只添加对角的起始元素，其中还要注意防止都相等的时候也会
            #重复打印元素
            if one == two:
                j = four
                res.append(matrix[i][j])
            else:
                for j in range(four,three,-1):
                    res.append(matrix[i][j])
            j = three
            if three == four:
                if one != two:
                    i = two
                    res.append(matrix[i][j])
            else:
                for i in range(two,one,-1):
                    res.append(matrix[i][j])
            one += 1
            two -= 1
            three += 1
            four -= 1
        return res
