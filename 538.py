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
    def inorder(self,root,lst):
        if root:
            self.inorder(root.left,lst)
            lst.append(root.val)
            self.inorder(root.right,lst)
        
    def neworder(self,root,lst,haha):
        if root:
            self.neworder(root.right,lst,haha)
            haha[0] += lst.pop()
            root.val = haha[0]
            self.neworder(root.left,lst,haha)
            
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        lst = []
        self.inorder(root,lst)
        self.neworder(root,lst,[0])
        return root
