# -*- coding: utf-8 -*- 
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be 
constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        dict记录每一个字符出现的次数，然后对magazine的字母做比较，如果出现，次数减1，次数减为0的话弹出该字符表示已经足够表示该字符了。
        如果最后dict为空，则能够构造出，否则false
        """
        dict = {}
        for num in ransomNote:
            dict[num] = dict.get(num,0) + 1
        for num in magazine:
            if num in dict:
                dict[num] -= 1
                if dict[num] == 0:
                    dict.pop(num)
        if dict == {}:
            return True
        return False

