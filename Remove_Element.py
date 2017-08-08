# -*- coding: utf-8 -*- 
'''
No.27
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #i记录符合条件的下标，j寻找符合条件的数，找到以后和i互换然后i+1
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
                continue
            if j > i:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i += 1
            j += 1
        return i
print Solution().removeElement([0], 0)