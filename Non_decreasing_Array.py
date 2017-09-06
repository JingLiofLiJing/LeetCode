# -*- coding: utf-8 -*-
'''
No.665
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
'''
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        3种情况考虑
          1.一开始就下降，则修正开始下标数值
          2.最后一个下降，修正最后一个下标数值
          3.中间（i）的一个数（i+1）下降，考虑i-1的数值（此时i+1和i-1都不会超出范围），如果i+1值大于等于i-1值则修正i的值，如果i+1的值小于i-1
            的值，修正i+1的值，最后减去可以修正次数use在判断即可。这样每次保证i+1之前的数字都满足要求再向后面迭代根据use判断
        """
        use = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                use -= 1      
                if use < 0:
                    return False
                if i == 0:
                    nums[i] = nums[i+1]
                elif i == len(nums) - 2:
                    nums[i+1] = nums[i]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                elif nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
            i += 1
        return True
        
        
