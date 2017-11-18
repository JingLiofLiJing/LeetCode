# -*- coding: utf-8 -*- 
'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def search(self,Node,depth):
        if Node == None:
            return depth
        depth += 1
        mx_left = self.search(Node.left,depth)
        mx_right = self.search(Node.right,depth)
        return max(mx_left,mx_right)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #search方法寻找从该深度的节点开始查找子节点最多有多深，最后返回给顶端
        return self.search(root,0)
