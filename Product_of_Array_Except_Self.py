# -*- coding: utf-8 -*- 
'''
No.238
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements 
of nums except nums[i].Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].
Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space 
complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        首先用all记录所有非0数的乘积，如果遇到0，记录0的个数，如果0的个数大于等于2次，则所有的元素都为0
        如果有一个为0，则带0的元素为其他非0的乘积all，其他的由于乘了0所以都是0，如果没有0出现，则每个数
        更新为总乘积除以自己原来的数即可。时间复杂度O（n），空间复杂度O（1）。
        """
        all = 1
        zero = -1
        for num in nums:
            if num != 0:
                all *= num
            else:
                zero += 1
        for i in range(0,len(nums)):
            if zero > 0:
                nums[i] = 0
            elif zero == 0:
                if nums[i] == 0:
                    nums[i] = all
                else:
                    nums[i] = 0
            else:
                nums[i] = all/nums[i]
        return nums
        
