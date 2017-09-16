# -*- coding: utf-8 -*- 
'''
No.560
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        假设（i，k）之间的值的和为k，则表示（0，k）值的和与（0，i-1）的值的和的差值正好为k，所以可以建立一个字典存储每一个下标从0到当前遍历位置i的数的
        总和m，并判断m-k的值是否在字典内的键中出现过（即之前0到某个下标之前所有数的和为m-k），如果出现了最后结果加上之前出现的次数即可。最后在在字典中
        记录此处的前面数字的总和。
        """
        #此处一开始存的0:1相当于total一开始什么都没加时的状态，用来确认是否直接从0到n的和等于k，而不用减掉小下标的数字和，之后正常更新
        #dic保存的是包括什么都没有的0:1以及每次遍历是前面数字的总和
        dic = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num
            res += dic.get(total - k,0)
            dic.setdefault(total,0)
            dic[total] += 1
        return res
        
