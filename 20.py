# -*- coding: utf-8 -*- 
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        #利用list模拟堆栈判断即可，先进先出，如果左边的直接进栈，右边的如果栈为空或者不匹配直接返回False，否则在判断堆栈是否为空，为空说明都匹配上了，否则为False
        """
        mstack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                mstack.append(i)
            elif len(mstack) > 0 and ((i == ')' and mstack[-1] == '(') or (i == ']' and mstack[-1] == '[') or (i == '}' and mstack[-1] == '{')):
                    mstack.pop()
            else:
                return False
        return mstack == []
        
        
        
   
