# -*- coding: utf-8 -*- 
'''
No.90
Given a collection of integers that might contain duplicates, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        首先判断是否为空，如果为空返回一个[[]]，否则先把第一个加进res，从第二个开始如果和前面的不重复，则res里的每一个并上该元素加到res后面形成
        新的res，此时记录原来res的末尾位置tmp=len（res），因为如果此时的元素如果和前面的相同的话，就不需要把res里每一个并上后进行添加，这样会有重复
        元素，应该先记录此时的末尾位置tmp2=len（res），从上一个tmp位置一直到tmp2的元素进行并上然后添加操作后再吧tmp更新为tmp即可。
        """
        res = [[]]
        tmp = 0
        if nums != []:
            nums.sort()
            for i in range(len(nums)):
                if i == 0:
                    res.append([nums[i]])
                else:
                    if nums[i] > nums[i-1]:
                        tmp = len(res)
                        for j in range(tmp):
                            res.append(res[j]+[nums[i]])
                    elif nums[i] == nums[i-1]:
                        tmp2 = len(res)
                        for j in range(tmp,tmp2):
                            #防止第一个数就重复造成的重复问题，后面的数重复的话不会进入此if内部
                            if res[j] != []:
                                res.append(res[j]+[nums[i]])
                        tmp = tmp2
        return res

print Solution().subsetsWithDup([1,2,2,3,4])
