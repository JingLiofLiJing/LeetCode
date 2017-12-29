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
        
  
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0 
        #j表示当前形成子串的开始位置
        j = maxd = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used:
                #如果存在重复的元素，首先更新或者确定序列开始边界，如果abcddb，当读到第二个d时，j会为4，表示开头变了，但是前面的abc还保存这之前的序列
                #在读到第二个d的时候，max方法就可以定位到目前的开始边界，可以看到b重复的边界仍然和d一样为4
                j = max(j,used[s[i]]+1)
            #更新最新的边界，与max方法对应
            used[s[i]] = i
            maxd = max(maxd,i-j+1)
        return maxd
