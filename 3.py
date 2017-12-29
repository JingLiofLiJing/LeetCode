# -*- coding: utf-8 -*- 
'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        首先判断空串，然后建立字符和下标的字典，记录读取过的不重复的字符，当读取到重复的字符时，比较更新之前的不重复的长度数end-start，
        然后将start移动到重复的字符的后一位并同时删除字典的记录，直到最后，当while循环结束时，最后一个子串还得再比较一次
        """
        if s == "":
            return 0 
        start =  0
        end =  1
        maxd = 0
        used = {s[start]:start}
        while end < len(s):
            if s[end] not in used:
                used[s[end]] = end
            else:
                maxd = max(maxd,end - start)
                while s[start] != s[end]:
                    del used[s[start]]
                    start += 1
                start += 1
            end += 1
        return max(maxd,end-start)
        
   
