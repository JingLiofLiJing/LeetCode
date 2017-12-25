# -*- coding: utf-8 -*- 
'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        #递归比较就好
        """
        if p == None and q == None:
            return True
        elif p == None or q== None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right)
