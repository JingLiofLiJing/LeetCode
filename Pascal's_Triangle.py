# -*- coding: utf-8 -*- 
'''
No.118
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
'''
class Solution(object):
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
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = self.getRow_Ok(i)
            res.append(row)
        return res
    
print Solution().generate(5)
        