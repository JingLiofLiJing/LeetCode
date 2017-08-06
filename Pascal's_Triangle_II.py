# -*- coding: utf-8 -*- 
'''
No.119
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
'''
from astropy.wcs.docstrings import row
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #对于每一次迭代，两头的数不变，中间的数由之前的数组加得到再组合成结果
        row0 = [1]
        i = 1
        while i <= rowIndex:
            row1 = []
            j = 1
            while j < i:
                row1.insert(j - 1, row0[j]+row0[j-1])
                j += 1
            row0 = row0[0:1] + row1 + row0[0:1]
            i += 1
        return row0
    
    #O（k）的解法
    def getRow_Ok(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #先多出第一位，然后后面从第1位到第len-1位和后面一位相加即可，正好额外用了k空间
        row = [1]
        i = 1
        while i <= rowIndex:
            row = row[0:1] + row
            j = 1
            while j < i:
                row[j] = row[j] + row[j+1]
                j += 1
            i += 1
        return row
print Solution().getRow_Ok(2)
# 1

# 1 1
# 
# 1 2 1 
# 1 5 10 10 5 1      5
# 1 6 15 20 15 6 1   6                       
# 1 3 3 1
# 
# 1 4 6 4 1
#1 5 10 10 5 1
