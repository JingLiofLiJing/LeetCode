
# -*- coding: utf-8 -*- 
'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        先判断周围最多8个点的live数量，然后进行判断，如果1的点死了先记为-1表示下一次为0（负号），活着不变。如果0的点活了变为2，还是死的话不变
        更新所有点状态之后再把-1变为0和2变为1即可
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                dead = 0
                if i - 1 >= 0:
                    if board[i-1][j] == 0 or board[i-1][j] == 2:
                        dead += 1
                    else:
                        live += 1
                    if j - 1 >=0:
                        if board[i-1][j-1] == 0 or board[i-1][j-1] == 2:
                            dead += 1
                        else:
                            live += 1
                    if j + 1 < n:
                        if board[i-1][j+1] == 0 or board[i-1][j+1] == 2:
                            dead += 1
                        else:
                            live += 1
                
                if i + 1 < m:
                    if board[i+1][j] == 0:
                        dead += 1
                    else:
                        live += 1
                    if j - 1 >=0:
                        if board[i+1][j-1] == 0:
                            dead += 1
                        else:
                            live += 1
                    if j + 1 < n:
                        if board[i+1][j+1] == 0:
                            dead += 1
                        else:
                            live += 1
                
                if j - 1 >=0 :
                    if board[i][j-1] == 0 or board[i][j-1] == 2:
                        dead += 1
                    else:
                        live += 1
                
                if j + 1 < n :
                    if board[i][j+1] == 0:
                        dead += 1
                    else:
                        live += 1 
                        
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
    
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                    
