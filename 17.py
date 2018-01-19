# -*- coding: utf-8 -*- 
'''
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        初始化一个字典对应数字和字符的对应关系，之后对于每一个输入的数字，分别与之前的结果拼接即可
        """
        dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res = []
        for st in digits:
            if res == []:
                #防止dict中的list随着res的变化而增大
                res = list(dict[st])
                continue
            end = len(res)
            for j in range(end):
                for i in range(len(dict[st])):
                    res.append(res[j]+dict[st][i])
            res = res[end:]
        return res
