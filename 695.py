# -*- coding: utf-8 -*- 
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''
class Solution(object):
    def searchisland(self,grid,i,j):
        if i >=0 and i < len(grid) and j >=0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.searchisland(grid,i-1,j) + self.searchisland(grid,i+1,j) + self.searchisland(grid,i,j-1) + self.searchisland(grid,i,j+1)
        return 0
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        迭代查找，dfs方法，当第一次遇到在格子里且为1的点，当做某岛屿的入口点，然后将此点置0防止重复计算（每个点也只会计算一次），然后递归对上下左右
        4个方向进行计算相加，最后做一下极大值比较就行
        """
        m = len(grid)
        n = len(grid[0])
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxarea = max(maxarea,self.searchisland(grid,i,j))
        return maxarea
