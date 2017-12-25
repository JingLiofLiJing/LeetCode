# -*- coding: utf-8 -*- 
'''
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.
'''
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n）算法：对于一个循环的子序列，其实是哪个数字都一样。inds代表下标集合，表示没有处理过的下标，res表示本次处理的循环包括的下标，while遍历
        找到所有循环的下标，下标重复时结束，inds-res得到未处理的下标，知道为空。
        """
        maxd = 0
        inds = [i for i in range(len(nums))]
        while inds != []:
            res = set()
            i = inds[0]
            while i not in res:
                res.add(i)
                i = nums[i]
            maxd = max(len(res),maxd)
            inds =  list(set(inds) - res)
        return maxd
        
