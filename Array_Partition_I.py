# -*- coding: utf-8 -*-
'''
No.561
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
'''
class Solution(object):
    '''
    #nums:数组           sum_1:总的大的数              sum_js:剩余的大数                   id：目前下标              limit:大数的值       reuslt:目前的结果
    def bj(self,nums,sum_1,sum_js,id,result,n):
        
        #此值在大数区域内
        sum_2 = sum_1 + 1
        sum_js2 = sum_js + 1
        result1 = result + nums[id]
        result4 = None
        id2 = id + 1
        if sum_2 == n:
            result4 =  result1
        elif id2 >= 2*n:
            result4 =  None
        else:
            lest = self.bj(nums,sum_2,sum_js2,id2,result1,n)
            if lest != None:
                result4 =lest
            
        #此值在小数区域内   
        sum_js3 = sum_js - 1
        id3 = id + 1
        result3 = None
        if sum_js3 < 0:
            result3 = None
        elif id3 >= 2*n:
            result3 = None
        else:
            lest2 = self.bj(nums,sum_1,sum_js3,id3,result,n)
            if lest2 != None:
                result3 =lest2
            
        if result3 == None and result4 ==None:
            return None
        elif result3 == None:
            return result4
        elif result4 ==None:
            return result3
        elif result4<result3:
            return result4
        else:
            return result3
        
            
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        all = 0
        for num in nums:
            all += num
        nums.sort()
        nums.reverse()
        #最大的数一定是在大叔里面
        if n == 1:
            return nums[1]
        sum_1 = 1
        sum_js = 1
        id = 1
        result = nums[0]
        result = self.bj(nums,sum_1,sum_js,id,result,n)
        return all-result
    '''
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
                        思路：假设每一对为(ai,bi),并且ai<=bi,有n对一共2n个数，则设Sum = a1+b1+a2+b2+.....+an+bn
                                    所求的是 jj=a1+a2+...+an，差值为cha=(b1-a1)+...+(bn-an),则2jj+cha=sum，jj=(sum-cha)/2
            jj最大，差越小，所以相邻的为一组差最小，即技术下标加起来即为答案
        """
        nums.sort()
        result = 0
        n = len(nums)/2
        for i in range(n):
            result += nums[2*i]
        return result
        
print Solution().arrayPairSum([1,22,3,-4,-52,6,67,123,-8,9,45,123123,-4535,564,-123123,878,2323,9879,-2323,8786,123123,-568568])
        