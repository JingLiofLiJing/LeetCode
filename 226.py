28 lines (26 sloc)  831 Bytes
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        #递归方法，深度优先，首先记录当前节点的子节点，然后将子节点赋值为倒转的递归函数返回节点即可
        """
        if root != None:
            l = root.left
            r = root.right
            root.left = self.invertTree(r)
            root.right = self.invertTree(l)
        return root
