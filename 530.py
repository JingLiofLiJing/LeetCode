# -*- coding: utf-8 -*- 
'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def souji(self,node,value,lst):
        if node == None:
            return lst
        lst.append(node.val - value)
        a = self.souji(node.left,value,[])
        b = self.souji(node.right,value,[])
        return a+b+lst
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        得到没一个元素相对于根节点的差值，然后排序相减再取最小值即可，这个适用于任何一种树
        """
        hecha =  self.souji(root,root.val,[])
        hecha.sort()
        for i in range(len(hecha)-1,0,-1):
            hecha[i] = hecha[i] - hecha[i-1]
        return min(hecha[1:])
        
