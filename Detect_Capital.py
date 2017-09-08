# -*- coding: utf-8 -*-
'''
No.520
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        #如果长度小于等于1则一定正确；否则先判断第一位，如果第一位大写，则后面全大写或者全小写；如果第1位小写，则后面全小写，
        出现大写即为错误。
        """
        if len(word) > 1:
            if word[0].isupper():
                for i in range(2,len(word)):
                    if (word[i].isupper() and not word[1].isupper()) or (word[i].islower() and not word[1].islower()):
                        return False
            else:   
                for i in range(1,len(word)):
                    if word[i].isupper():
                        return False
        return True
        
