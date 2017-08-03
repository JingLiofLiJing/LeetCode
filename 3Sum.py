# -*- coding: utf-8 -*- 
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
'''
class Solution(object):
    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num.sort()
        res = []
        for i in range(len(num)-2):
            #以最左边的来划分,相同的数字只算第一个防止重复
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res

S = Solution()
print S.threeSum([-1, 0, 1, 2, -1, -4])