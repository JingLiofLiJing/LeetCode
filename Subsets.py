# -*- coding: utf-8 -*- 
'''
No.78
Given a set of distinct integers, nums, return all possible subsets.
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #因为数组内数字都不同，所以每次记录一下结果数组的长度，然后数组的每个元素并上新的数字再加到后尾即可
        """
        res = [[]]
        i = 0
        while i < len(nums):
            index = len(res)
            for j in range(index):
                res.append(res[j]+[nums[i]])
            i += 1
        return res
    
print Solution().subsets([1,2,3])
