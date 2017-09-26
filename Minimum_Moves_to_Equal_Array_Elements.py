# -*- coding: utf-8 -*- 
'''
No.453
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing n - 1 elements by 1.
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        首先，最小的数在进行累加的过程中一直都是被加1的对象，所以假设至少加了m次，加之前的最小值为a，所有元素和为b,数组长度为n
        则 b + m(n-1) = (a+m)*n,化简则得到 m = b - an
        """
        a,b = min(nums),sum(nums)
        n = len(nums)
        return b-a*n
        
