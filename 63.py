# -*- coding: utf-8 -*- 
'''
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        动态规划方法：如果碰到阻碍的地方，则其可达数直接置位0，后面的点计算可达数时遇到阻碍的地方默认为加0，即不可行。从上到下从左到右进行
        遍历，即可
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        canwalk = [[1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    canwalk[i][j] = 0
                elif i == 0 and j > 0:
                    canwalk[i][j] =  canwalk[i][j-1]
                elif j == 0 and i > 0:
                    canwalk[i][j] =  canwalk[i-1][j]
                elif i > 0 and j > 0:
                    canwalk[i][j] =  canwalk[i-1][j] + canwalk[i][j-1]
        return canwalk[-1][-1]
