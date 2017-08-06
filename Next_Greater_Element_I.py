# -*- coding: utf-8 -*- 
'''
No.496
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in findNums:
            #下标清0，从头开始找位置，并设结果为找不到
            i = 0
            numres = -1
            while i < len(nums):
                if nums[i] == num:
                    j = i+1
                    while j < len(nums):
                        if nums[j] > num:
                            numres = nums[j]
                            break
                        j += 1
                    res.append(numres)
                i += 1
        return res

print Solution().nextGreaterElement([4,1,2], [1,3,4,2])
            
            