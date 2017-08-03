# -*- coding: utf-8 -*- 
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
                        相同的数取异或为0，所以所有数字异或后剩下的就是单独的数字
        """
        for i,j in enumerate(nums):
            if i==0:
                nums[i] = 0^j
            else:
                nums[i] ^= nums[i-1]  
        return nums[-1]
    
print Solution().singleNumber([1,3,-2,4,-1,4,-2])