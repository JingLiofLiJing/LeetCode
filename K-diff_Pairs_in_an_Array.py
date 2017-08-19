#-*- coding:utf-8 -*-
'''
No.532
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
'''
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #利用字典，数组值做键，出现的次数作为值，k= 0时一个数出现至少两次结果+1，k > 0 时 间隔为k的两个数存在时结果+1
        #其中k<0不符合条件，所以去除（WTF？）
        if k < 0:
            return 0
        result = 0
        dict = {}
        for i in range(len(nums)):
            dict.setdefault(nums[i],0)
            dict[nums[i]] += 1
        a = dict.keys()
        a.sort()
        for num in a:
            if k == 0:
                if dict[num] >= 2:
                    result += 1
            elif num + k in dict:
                result += 1
        return result
print Solution().findPairs([1,2,3,4,5],-1)

