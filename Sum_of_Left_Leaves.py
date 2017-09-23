# -*- coding: utf-8 -*-
'''
No.404
Find the sum of all left leaves in a given binary tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self,sum,node,lr):
        if node == None:
            return sum
        if node.left == None and node.right == None and lr == 'l':
            sum += node.val
            return sum
        sum1 = self.search(sum,node.left,"l")
        sum2 = self.search(sum1,node.right,"r")
        return sum2
            
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        如果为空或者单节点则返回0，然后分别遍历左子树的结果并将结果带入右子树的遍历得到最终结果
        同时设置l和r标记辨别左节点
        """
        sum = 0
        if root == None:
            return sum
        if root.left or root.right:
            sum1 = self.search(sum,root.left,"l")
            sum = self.search(sum1,root.right,"r")
        return sum
        
