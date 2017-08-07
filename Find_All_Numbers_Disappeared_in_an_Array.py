# -*- coding: utf-8 -*- 
'''
No.448
Given an array of integers where 1 �� a[i] �� n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        #每个数组的数字表示那个下标被使用过了，使用过下标的数字取反即负数，下标用abs绝对值取，如果下标对应值为负数的话说明该下标有双份，最后正数值对应的下标即为没有出现过的下标
        for index in nums:
            if nums[abs(index)-1] > 0:
                nums[abs(index)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
 
print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
# 1 2 3 4 5 6 
# 3 5 1 3 2 5