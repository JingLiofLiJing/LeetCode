# -*- coding: utf-8 -*- 
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
class Solution(object):
    def search(self,s,i,j,maxd,start,end):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        lens = j - i - 1
        if lens <= maxd:
            return maxd,start,end
        else:
            return lens,i+1,j
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        #暴力求解，首先全局最大长度和开头结尾，从开头到倒数第二个遍历，分别找偶数对的序列和奇数对的序列，如果长度超过则记录即可
        """
        maxd = 0
        start = end = 0
        if len(s) < 2:
            return s
        for i in range(len(s)-1):
            maxd,start,end = self.search(s,i,i+1,maxd,start,end)
            maxd,start,end = self.search(s,i,i,maxd,start,end)
        return s[start:end]
