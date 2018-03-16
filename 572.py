# -*- coding: utf-8 -*- 
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self,s,t):
        if not (s or t):
            return True
        elif not s or not t or s.val != t.val:
            return False
        return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None or t == None:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
            
