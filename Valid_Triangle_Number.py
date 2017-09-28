coding: utf-8 -*-
'''
No.611
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from 
the array that can make triangles if we take them as side lengths of a triangle.
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #记录每个数字出现的次数
        res = {}
        sumn = 0
        for num in nums:
            res[num] = res.get(num,0) + 1
        inds = res.keys()
        inds.sort()
        for i in range(len(inds)):
            if inds[i] == 0:
                continue
            #判断等边三角形
            if res[inds[i]] >= 3:
                sumn += res[inds[i]]*(res[inds[i]]-1)*(res[inds[i]]-2)/6
            j = i + 1
            while j < len(inds):
                #判断等腰三角形
                sumn += res[inds[i]] * res[inds[j]]*(res[inds[j]]-1)/2
                if 2*inds[i] > inds[j]:
                    sumn += res[inds[j]] * res[inds[i]]*(res[inds[i]]-1)/2
                maxn = inds[i] + inds[j]
                minn = abs(inds[i]-inds[j])
                k = j + 1
                while k < len(inds):
                    #判断一般三角形
                    if inds[k] < maxn and inds[k] > minn:
                        sumn += res[inds[i]]*res[inds[j]]*res[inds[k]]
                    k+=1
                j+=1
        return sumn
    
    
    def better(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #首先对数组进行排序，i从头到导数第二个，j从i后面第一个开始，k从j后面第一个开始，在i<j<k的同时只要满足
        #nums[i]+nums[j]>nums[K]的k值都满足要求（因为k下标值大于i和j下标值，自然大于两者的差），当找到最
        #后一个满足的k时，则目前的i、j情况下共有k-j-1个满足的三元组，所以遍历一遍i和j直到最后就能得到所有满足
        #的元组，复杂度o（n^2），为上面的改进
        sumn = 0
        nums.sort()
        for i in range(0,len(nums)-2):
            if nums[i] == 0:
                continue
            j = i + 1
            #k不在j循坏里是因为当上一个k到达第一个不满足要求的点的时候，j+1时k前面的值仍然满足nums[i]+nums[j]>nums[K]
            #只是j可能变大了，所以k继续往后查找，这样可以减少时间开销，并且当存在条件j>=k的时候，通过nums[i]+nums[j]>nums[K]
            #的比较k最后会大于j（第一个不满足条件的k处），所以不会产生冲突。
            k = j + 1
            while j < len(nums) - 1:
                while k < len(nums):
                    if nums[i] + nums[j] > nums[k]:
                        k += 1
                    else:
                        break
                sumn += k - 1 - j
                j += 1
        return sumn
        
        
print Solution().triangleNumber([2,2,3,4,5,6,7,8,8,9,5])
