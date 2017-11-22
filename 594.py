
# -*- coding: utf-8 -*- 
'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
'''
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        #哈希表记录每个数字出现的次数然后累加判断即可
        """
        dict = {}
        maxl = 0
        for num in nums:
            dict[num] = dict.get(num,0) + 1
        for key in dict:
            if key+1 in dict:
                maxl = max(maxl,dict[key]+dict[key+1])
        return maxl
