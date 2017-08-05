# -*- coding: utf-8 -*-
'''
No.345
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yy = ["a","e","i","o","u"]
        #返回一个新的str，而不改变原来的str
        ss = list(s)
        dict = {}
        for i in range(len(ss)):
            if ss[i].lower() in yy:
                dict[i] = ss[i]
        #dict是无序的，所以取出键对（元音下标）进行排序再进行替换
        a = dict.keys()
        a.sort()
        start = 0
        end = len(a)-1
        while start < end:
            ss[a[start]] = dict[a[end]]
            ss[a[end]] = dict[a[start]]
            start += 1
            end -= 1
        return "".join(ss)
    
print Solution().reverseVowels("race a car")

