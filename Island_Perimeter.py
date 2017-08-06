# -*- coding: utf-8 -*- 
'''
No.463
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water 
inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, 
width and height don't exceed 100. Determine the perimeter of the island.
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #不一定是方阵，所以分别统计长宽的数值
        lg = len(grid)
        lg2 = len(grid[0])
        up = down = left = right = 0
        for i in range(lg):
            for j in range(lg2):
                if grid[i][j] == 1:
                    #分别根据矩阵临界或者上个网格的值判断是否属于岛屿边界
                    if i == 0 or grid[i-1][j] == 0:
                        up += 1
                    if i == lg-1 or grid[i+1][j] == 0:
                        down += 1
                    if j == 0 or grid[i][j-1] == 0:
                        left += 1
                    if j == lg2 - 1 or grid[i][j+1] == 0:
                        right += 1
        return up+down+left+right

print Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])