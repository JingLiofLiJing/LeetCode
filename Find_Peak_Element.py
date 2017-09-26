# -*- coding: utf-8 -*- 
'''
No.162
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        记录最大数及其位置
        """
        if len(nums) == 0:
            return 0
        i = j = tmp = 0
        res = -1
        while i < len(nums):
            while j < len(nums):
                tmp += nums[j]
                if tmp >= s:
                    if res == -1:
                        res = j-i+1
                    elif j-i+1 <res:
                        res = j-i+1
                    break
                j += 1
            if j == len(nums):
                break
            tmp = tmp - nums[i] - nums[j]           
            i+=1
        if res == -1:
            return 0
        return res
print Solution().minSubArrayLen(11, [1,2,3,4,5])
