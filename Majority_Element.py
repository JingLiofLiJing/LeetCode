# -*- coding: utf-8 -*- 
'''
No.169
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #建立一个堆栈即可，相同的入栈，不同的出栈一个，最后栈内的就是答案
        a = [nums[0]]
        i = 1
        while i < len(nums):
            if len(a) == 0:
                a.append(nums[i])
            elif nums[i] == a[0]:
                a.append(nums[i])
            else:
                a.pop()
            i += 1
        return a[0]
    
    def majorityElement_noextraarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #将堆栈内建到数组中，默认为第一个数，往后如果一样，end向后扩展并修改end处值为1，即进栈，如果遇到不一样的出站，如果end<start,即栈为空，则
        #将堆栈向后建立，在第i+1处初始化并把i设置为i+2继续查找，最后在堆栈的一定是结果,这样会改变原来数组
        start = 0
        end = 0
        i = 1
        while i < len(nums):
            if nums[start] == nums[i]:
                end += 1
                nums[end] = nums[start]
            elif nums[start] != nums[i]:
                end -= 1
                if end < start:
                    start = end = i+1
                    i += 2
                    continue
            i += 1
        return nums[start]
        
        

print Solution().majorityElement_noextraarray([6,53,53,96,45,79,53,58,53,90,40,53,53,1,53,53,89,53,33,27,53,53,84,42,53,53,87,51,66,53,28,53,53,53,50,39,36,48,19,74,38,53,42,53,99,53,80,53,53,53,53,96,78,52,24,53,53,53,53,64,10,53,53,53,53,82,53,53,53,22,53,53,67,53,53,53,53,53,67,53,19,99,53,53,21,53,69,53,53,53,52,53,96,53,53,51,81,62,4,6])