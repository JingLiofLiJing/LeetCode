# -*- coding:utf-8 -*-  
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #动态规划解法：随着遍历这个数组，在到每一个位置的时候，弄一个局部最大L值，代表以当前位置为结尾的最大子串，比如说我遍历到第i个，
        #那么以第i个为结尾的最大子串就是我们要求的L。
        #比如这个题目：-2 , 1, −3,4,−1,2,1,−5,4 
        #位置0，L=x=-2，没得选 
        #位置1，要以x=1为结尾的最大的，那肯定不要带上之前的-2,只要1就好L=x=1 
        #位置2，因为本身x=-3，加上上一个位置L 是正数1，所以L=L+x=-3+1=-2。 
        #下面以此类推得到：
        #对应的L应该是： 
        #-2, 1, -2,4,3,5,6,-1,3
        #而全局最大值G就是我们最终想要的结果， 
        #肯定这个全局最大值出自局部最大值。 
        #（因为全局最大的那个子串的结尾肯定在数组里，言外之意就是不管怎么样这个G都肯定出自L） 
        #最后找到最大的那个L就是我们想要的G了。
        l = g = -1000000000 #设置最小数存每一阶段的局部最大值
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g
    
    def divide(self,nums,left,right):
      if left == right:
        return nums[left]
      elif left + 1 == right:
        return max(nums[left],nums[right])
      mid = (left+right)/2
      lmax = self.divide(nums,left,mid)
      rmax = self.divide(nums,mid+1，right)
      
      mmax = nums[mid]
      tmp = mmax
      i = mid - 1
      while i >= left:
        tmp += nums[i]
        if tmp > mmax:
          mmax = tmp
        i -= 1
      i = mid+1
      tmp = mmax
      while i <= right:
        tmp += nums[i]
        if tmp > mmax:
          mmax = tmp
         i += 1
      retrun max(lmax,rmax,mmax)
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #动态规划解法:将数组分为两半，则最大的子集要不是都在左半部分，要不就在右半部分，要不都在，如果都在的话则一定包括
        #中间的元素，左右部分的值可以递归求解，都在的部分的值去中间的值为初始值依次向左右伸展并记录和的最大值在比较即可
        #因为对于从中间开始找的算法，最好的子集两边一开始肯定都是负数，最优子集里面的子集无论和左边延伸出去的多少个值相加
        #结果都会小于对应子集的和，所以对中间开始找的算法，先用中间的数字进行开始，分别依次加上左右边的值并保存最大值，得
        #到的值就是所求的值。
        return self.divide(nums,0,len(nums)-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
