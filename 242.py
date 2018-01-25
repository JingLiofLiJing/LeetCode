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
