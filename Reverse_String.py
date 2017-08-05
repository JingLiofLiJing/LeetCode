# -*- coding: utf-8 -*- 
'''
No.344
Write a function that takes a string as input and returns the string reversed.
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #使用双向指针能减少一半的时间，直接用单指针会时间溢出
        ls = len(s) - 1
        ss = 0
        res = [""]*len(s)
        while ls > ss:
            res[ss] = s[ls]
            res[ls] = s[ss]
            ss += 1
            ls -= 1
        if ss == ls:
            res[ss] = s[ss]
        return "".join(res)
    
    
    
    
    