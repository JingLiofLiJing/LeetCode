# -*- coding: utf-8 -*- 
'''
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        #哈希表对比即可
        """
        if len(s) != len(t):
            return False
        dict = {}
        for v in s:
            dict[v] = dict.get(v,0) + 1
        for v in t:
            if v not in dict:
                return False
            dict[v] -= 1
            if dict[v] == 0:
                del dict[v]
        return dict == {}

    
    class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        unicode情况
        """
        if len(s) != len(t):
            return False
        dict = {}
        i = 0
        word = ""
        while i < len(s):
            if s[i] == '\\':
                dict[s[i:i+6]] = dict.get(s[i:i+6],0) + 1
                i += 6
            else:
                dict[s[i]] = dict.get(s[i],0) + 1
                i += 1
        i = 0
        while i < len(t):
            if t[i] == '\\':
                word = dict[t[i:i+6]]
                i += 6
            else:
                word = t[i]
                i += 1
            if word not in dict:
                return False
            dict[word] -= 1
            if dict[word] == 0:
                del dict[word]
        return dict == {}
        
