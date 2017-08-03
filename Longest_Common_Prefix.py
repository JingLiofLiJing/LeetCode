# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.
第一个分别和后面的求最长前缀，然后取最短为答案
'''
class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = None
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        index = 1
        #第一个字符串依次和后面的比较，取结果的最短即为答案
        while index < len(strs):
            result = self.find(strs[0],strs[index])
            if index == 1:
                res = result
            else:
                if len(result) < len(res):
                    res = result
            index += 1
        return "".join(res)
            
    
    def find(self,a1,a2):
        length = len(a1)
        if len(a1) > len(a2):
            length = len(a2) 
        end = 0
        while end < length:
            if a1[end] != a2[end]:
                break
            else:
                end += 1
        return a1[0:end]
        
print Solution().longestCommonPrefix(["A","ABC","Abcd"])