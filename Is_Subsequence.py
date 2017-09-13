# -*- coding: utf-8 -*-
'''
No.392
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. 
  t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting 
  some (can be none) of the characters without disturbing the relative positions of the remaining 
  characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution(object):
    def bj(self,s,t,s_ind,t_ind):
        while s_ind >= 0 and s[s_ind] != t[t_ind]:
            s_ind -= 1
        if s_ind < 0:
            return False
        if t_ind == 0:
            return True
        else:
            return self.bj(s,t,s_ind-1,t_ind-1)
        
        
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        #动态规划，从后往前匹配，先匹配最后一个，如果找到，则在匹配前一个，同时两个匹配序列不断压缩
        最后bj（）中先看s_ind是否小于0防止误判在index=0处正好两者最后一个元素相匹配
        """
        if s == "":
            return True
        if self.bj(t,s,len(t)-1,len(s)-1):
            return True
        return False

print Solution().isSubsequence("abc","ahbgdc")
        
