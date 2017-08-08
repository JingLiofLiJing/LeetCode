# -*- coding: utf-8 -*- 
'''
No.167
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind1 = 0
        ind2 = len(numbers) - 1
        while numbers[ind1] + numbers[ind2] != target:
            if numbers[ind1] + numbers[ind2] < target:
                ind1 += 1
            else:
                ind2 -= 1
        return [ind1+1,ind2+1]
                
                
a = [2,3,4]
b = 6
print Solution().twoSum(a, b)