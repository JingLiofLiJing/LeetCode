# -*- coding: utf-8 -*- 
'''
No.557
Given a string, you need to reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order.
'''
class Solution(object):
    def rvs(self,s,start,end):
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

    def reverseWords(self,s):
        """
        :type s: str
        :rtype: str
        #每一次记录单词的起始和终点位置再进行反向即可
        """
        i = 0
        ss = list(s)
        while i < len(ss):
            start = 0
            end = 0
            if ss[i] != ' ':
                start = i
                while i < len(ss) and ss[i] != " ":
                    i += 1
                end = i - 1
                self.rvs(ss,start,end)
            i += 1
        return ''.join(ss)
        
