# -*- coding: utf-8 -*- 
'''
No.500
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {1:["q","w","e","r","t","y","u","i","o","p"],
                2:["a","s","d","f","g","h","j","k","l"],
                3:["z","x","c","v","b","n","m"]
            }
        res = []
        for word in words:
            #将所有单词字母变成小写进行比较
            word_low = word.lower()
            line = 0
            #保证单个字母的时候符合要求
            same = True
            for j in range(len(word_low)):
                if j==0:
                    for index,value in dict.items():
                        if word_low[j] in value:
                            line = index
                            break
                else:
                    for index,value in dict.items():
                        if word_low[j] in value:
                            if index != line:
                                same = False
                                break
            if same == True:
                res.append(word)
        return res

print Solution().findWords(["Hello", "Alaska", "Dad", "Peace","a","a"])