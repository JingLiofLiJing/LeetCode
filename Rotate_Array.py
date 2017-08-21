#-*- coding:utf-8 -*-
'''
No.189
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''
class Solution(object):
    def reversess(self,nums,start,end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # a1 a2 ..... an 如果向后转k位 变成 a(n-k+1)  a(n-k+2) ... a(n-1) an  a1 a2 .....ak-2 ak-1
        #a(n-k+1)  a(n-k+2) ... a(n-1) an 倒转和 a1 a2 .....ak-2 ak-1倒转拼接起来正好是a1到an的倒转
        #所以先把整个数组倒转，再倒转前k项目和剩下的项即可
        #如果k>len(nums)，那么前面k整数倍的翻转是多余的
        k = k % len(nums)
        self.reversess(nums,0,len(nums)-1)
        self.reversess(nums,0,k-1)
        self.reversess(nums,k,len(nums)-1)
        return nums


print Solution().rotate([1,2,3,4,5,6,7],3)