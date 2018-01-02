# -*- coding: utf-8 -*- 
'''
Given a collection of distinct numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    
    def search(self,nums):
        if len(nums) == 1:
            yield [nums[0]]
        for i in xrange(len(nums)):
            left = nums[:i] + nums[i+1:]
            for res in self.search(left):
                yield [nums[i]]+res
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        辣鸡方法：相当于遍历，利用递归方法得到后面的所有排列再和开始的元素并起来得到不同的排列
        """
        res = []
        for i in self.search(nums):
            res.append(i)
        return res
        
    
    #一下为另一种方法，首先1234放进去，然后对于123的情况，去掉3，放4变成124再得到1234，这时候123和124遍历完成，再12变成13和14进行遍历，直到所有都
    #遍历完成。
    def haha(self,lst,temp,nums):
        if len(temp) == len(nums):
            #引用传递会随着递归改变值，所以这里拷贝了一份使得结果不变
            lst.append(list(temp))
        else:
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                self.haha(lst,temp,nums)
                temp.pop()
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        self.haha(a,[],nums)
        return a
    
    
        
    
