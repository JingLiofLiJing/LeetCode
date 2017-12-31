# -*- coding: utf-8 -*- 
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2].
Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        规律解法，首先先对start：end的元素拼接在后面，然后再拼接对start：end的元素取+1，拼接时判断是否res长度等于num+1
        """
        res = [0]
        start = 0
        end = 1
        #0表示原始拼接，1表示加1拼接，因为初始化为[0],由+1拼接开始
        sym = 1
        while True:
            for i in range(start,end):
                if len(res) == num + 1:
                    return res
                res.append(res[i]+sym)
            if sym:
                start = end
                end = len(res)
            sym = 1 - sym
            
            
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        和上述类似，i下标的值等于i/2下标数字的值后面加0或者1，与i下标的数字二进制最后一位相等
        """
        f = [0 for i in range(num+1)]
        for i in range(1,num+1):
            f[i] = f[i >> 1] + (i & 1);
        return f
