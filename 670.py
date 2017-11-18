# -*- coding: utf-8 -*- 
'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
Return the maximum valued number you could get.
'''
class Solution(object):
    def swap(self,a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        #从左到右进行替换，每次找到当前位置右边的子序列的最大值，然后匹配最右边的该最大值的位置，进行替换即可
        nd = list(str(num))
        lg = len(nd)
        for i in range(lg-1):
            mx = max(nd[i+1:])
            if nd[i] >= mx:
                continue
            pos = str(num).rfind(mx)
            self.swap(nd,i,pos)
            break
        return int(''.join(nd))
