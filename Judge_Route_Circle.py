# -*- coding: utf-8 -*- 
'''
No.657
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are 
R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        两个变量分别记录左右位置和上下位置偏移，上左加1，下右减1，最后判断是否回到原点即可
        """
        sx = 0
        zy = 0
        lst = list(moves)
        for mv in moves:
            if mv == "L":
                zy += 1
            elif mv == "R":
                zy -= 1
            elif mv == "U":
                sx += 1
            elif mv == "D":
                sx -= 1
        if not sx and not zy:
            return True
        else:
            return False
            
            
