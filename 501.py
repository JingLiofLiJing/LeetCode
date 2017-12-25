# -*- coding: utf-8 -*- 
'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def ad(self,node,dict1,maxd):
        if node == None:
            return dict1,maxd
        dict1[node.val] = dict1.get(node.val,0) + 1
        maxd = max(maxd,dict1[node.val])
        dict1,maxd = self.ad(node.left,dict1,maxd)
        dict1,maxd = self.ad(node.right,dict1,maxd)
        return dict1,maxd
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        #遍历树得到次数字典，并记录最大次数，然后提取最大次数对应的数字即可
        """
        dict1 = {}
        maxd = 0
        dict1,maxd = self.ad(root,dict1,maxd)
        res = [i for i,v in dict1.items() if v==maxd]
        return res
        
