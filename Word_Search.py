# -*- coding: utf-8 -*- 
'''
No.79
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically 
eighboring. The same letter cell may not be used more than once.
'''
class Solution(object):
    #递归检查方法，直到word最后一位匹配
    def find(self,board,word,index,i,j,mb):
        #超出词汇表边界，则中断
        if i < 0 or i>=len(board) or j <0 or j>=len(board[0]):
            return False
        #元素被使用过，中断
        if mb[i][j] == 1:
            return False
        if word[index] != board[i][j]:
            return False
        #最后一位匹配，则找到
        if index == len(word) - 1:
            return True
        else:
            mb[i][j] = 1
            if self.find(board,word,index+1,i-1,j,mb):
                return True
            if self.find(board,word,index+1,i+1,j,mb):
                return True
            if self.find(board,word,index+1,i,j+1,mb):
                return True
            if self.find(board,word,index+1,i,j-1,mb):
                return True
            #如果四个方向都不匹配，则此路不通，注销掉次元素的使用标记，防止其他路匹配时
            #错误标记的影响
            mb[i][j] = 0
            return False
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #先天不成立的条件
        if board == [] or word == "":
            return False
        #记录元素的使用情况
        mb = []
        for i in range(len(board)):
            xx = []
            for j in range(len(board[0])):
                xx.append(0)
            mb.append(xx)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find(board,word,0,i,j,mb):
                    return True
        return False

print Solution().exist(["CAA","AAA","BCD"],"AAB")
