# -*- coding: utf-8 -*-
'''
No.667
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
If there are multiple answers, print any of them.
'''
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        #确定K值之后，开始的1到k+1一共k+1个数可以形成题目所说的有k个不同差值的序列，具体构造如下
        #左边第一个1，右边第一个k+1,左边第二个2，右边第二个k-1，左边第三个3.....直到左边等于右边位置，
        #这样得到的序列包含k个不同的差值（1到k），后面的按顺序排列，除了第一个数和左边k+1个数的序列的
        #最后一个数的差值最多为k，其他的差值都为1，则满足要求。
        """
        i = 1
        j = k + 1
        res = []
        left = True
        while i <= j:
            if left:
                res.append(i)
                i += 1
                left = False
            else:
                res.append(j)
                j -= 1
                left = True
        for i in range(k+2,n+1):
            res.append(i)
        return res
