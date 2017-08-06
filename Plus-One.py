# -*- coding: utf-8 -*- 
'''
No.66
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #从末尾开始计算，一开始设进位为1表示加1，后面的根据值改变进位，最高位考虑10扩展
        length = len(digits)
        i = length - 1
        jinwei = 1
        while i >= 0:
            digits[i] += jinwei
            if digits[i] == 10:
                jinwei = 1
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
            else:
                jinwei = 0
            i -= 1
        return digits
    
print Solution().plusOne([0])