# -*- coding: utf-8 -*-
'''
No.74
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
class Solution(object):
    '''
    2分法搜索目标数字（已经确定所在数组的情况下），
    如果start==end下还不能匹配，则查找失败
    '''
    def bs(self,lst,target,start,end):
        if start <= end:
            mid = (start+end)/2
            if lst[mid] == target:
                return True
            elif lst[mid] > target:
                return self.bs(lst,target,start,mid-1)
            else:
                return self.bs(lst,target,mid+1,end)
        return False
        
    '''
    2分法搜索在哪一行
    当找数字一样找，最后当start和end相等时，如果mid大的话，则返回mid-1一定比target小，所以mid-1为行的序号，如果mid小的话则返回mid
    所在的行
    '''
    def bs2(self,matrix,target,start,end):
        if start <= end:
            mid = (start+end)/2
            if matrix[mid][0] == target:
                return -1
            elif start == end:
                if matrix[mid] < target:
                    return mid
                else:
                    return mid - 1
            elif matrix[mid] > target:
                return self.bs2(matrix,target,start,mid-1)
            else:
                return self.bs2(matrix,target,mid+1,end)
            
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        2分法进行行查找和数字查找，复杂度o（logn）
        """
        if matrix == [] or len(matrix[0]) == 0:
            return False
        i = 0
        while i < len(matrix):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                break
            i += 1
        if i == 0:
            return False
        lst =  matrix[i - 1]
        # ind = self.bs2(matrix,target,0,len(matrix) - 1)
        # if ind < 0:
        #     return False
        # else:
        #     lst = matrix[ind]
        return self.bs(lst,target,0,len(lst) - 1)
        
