# -*- coding: utf-8 -*-
'''
No.64
Given a m x n grid filled with non-negative numbers, find a path from top 
left to bottom right which minimizes the sum of all numbers along its path.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        明显的动态规划问题，因为没有list嵌套，所以直接用used = grid[:][:]模拟深拷贝list
        对于第一行和第一列来说，到达的最优值依次把前面的相加就好，而剩下的[1:][1:]来说，由于只
        有向右走和向下走两种方法，所以只需要比较[i-1][j]和[i][j-1]的最小值再加上grid[i][j]
        的值就，此处used[i][j]表示从左上角到i，j处的最短开销。
        """
        if grid == []:
            return 0
        used = grid[:][:]
        xia = len(grid)
        you = len(grid[0])
        for i in range(1,xia):
            used[i][0] += used[i-1][0]
        for i in range(1,you):
            used[0][i] += used[0][i-1]
        for i in range(1,xia):
            for j in range(1,you):
                used[i][j] += min(used[i-1][j],used[i][j-1]) 
        return used[-1][-1]    


print Solution().minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]])
