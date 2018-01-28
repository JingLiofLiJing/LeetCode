# -*- coding: utf-8 -*- 
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
class Solution(object):
    def searchmin(self,n,lst):
        i = 1
        minx = n
        while i*i <= n:
            minx = min(minx,lst[n-i*i]+1)
            i += 1
        return minx
        
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        动态规划的方法，从1到n递归，lst存的为每个数对应方法使用的最少个数，对于第m个数来说，如果有一个元素k，则m-k*k的数的最小组成已经
        由之前的计算保存了，所以可以直接饮用。
        """
        lst = [0]
        for i in range(1,n+1):
            lst.append(self.searchmin(i,lst))
        return lst[-1]
            
            
            
    def findsqrt(self,n):
        j = 0
        while j*j <= n:
            j+=1
        return j-1
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        根据四平方定理，任何一个正数可以由最多4个非0正数的平方和组成，特别的是，当n除8余7时，一定为4个。首先先简化数，如果能被4整除则除4
        因为假如b=2a，a为平方和，则b的平方和每一项为a的2倍，两者的结果不变。然后寻找是否为两个数的平方和，如果是，如果有0的平方，则返回1
        否则返回2，都不是的话返回3.
        """
        while n%4 == 0:
            n /= 4
        if n%8 == 7:
            return 4
        a = 0
        while a*a <= n:
            res = n - a*a
            b = self.findsqrt(res)
            if a*a + b*b == n:
                if a==0 or b==0:
                    return 1
                else:
                    return 2
            a += 1
        return 3
