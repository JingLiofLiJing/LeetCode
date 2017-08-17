# -*- coding:utf-8 -*-
'''
No.414
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #o(nlogn)
        dict = {}
        for i in range(len(nums)):
            dict.setdefault(nums[i],0)
            dict[nums[i]] += 1
        a = dict.keys()
        a.sort()
        if len(a) < 3:
            return a[-1]
        else:
            return a[-3]

    #o(n) complexity
    def on(self,nums):
        #num1 最大的数,num2第二大的数字，num3第三大的数字
        num1 = None
        num2 = None
        num3 = None
        for num in nums:
            #如果都有的话过滤掉，直接从下一个继续
            if num == num1 or num==num2 or num == num3:
                continue
            #如果比第一个大或者第一个为空，数字向下移位
            if num1 == None:
                num1 = num
            elif num > num1:
                num3 = num2
                num2 = num1
                num1 = num
            # 如果比第二个大或者第二个为空，从第二个开始向下移位
            elif num2 == None:
                num2 = num
            elif num > num2:
                num3 = num2
                num2 = num
            #否则直接替换第三个大的数
            elif num3 == None:
                num3 = num
            elif num > num3:
                num3 = num
        if num3 == None:
            return num1
        return num3

print Solution().on([1,2,2,5,3,5])
