# -*- coding: utf-8 -*- 
'''
Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        num = 0
        #堆栈
        temp = ""
        #a为层叠的数字记录，b为层叠的[位置记录
        a = []
        b = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                #此处记录没有数字单独出现的字符串
                if temp != "" and '[' not in temp:
                    res += temp
                    temp = ""
                num = num*10 + int(s[i])
            elif s[i].isalpha():
                temp += s[i]
            elif s[i] == '[':
                #记录重叠时之前的数字和[位置
                temp += s[i]
                a.append(num)
                num = 0
                b.append(len(temp) - 1)
            elif s[i] == ']':
                #最近的一次[]对出栈，并扩展为所需要的形式
                j = b.pop() 
                temp = temp[:j] + a.pop()*temp[j+1:]
                if b == []:
                    res += temp
                    temp = ""
            i += 1
        return res + temp
        
        
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        更好的方法：stack堆栈，每当遇到字母时，堆栈最后一个的字符串加上，遇到[时添加新的栈元素，表示该层所包括的字符串和重复次数，
        遇到]时，最内一层出栈，次数乘上字符串加到父级的[]字符串里头，最后stack[-1][0]即为所求。
        """
        stack = [["",1]]
        num = ""
        for v in s:
            if v.isdigit():
                num += v
            elif v.isalpha():
                stack[-1][0] += v
            elif v == '[':
                stack.append(["",int(num)])
                num = ""
            elif v == ']':
                _s,_n = stack.pop()
                stack[-1][0] += _n * _s
        return stack[-1][0]
        
    
    
