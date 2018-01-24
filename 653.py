# -*- coding: utf-8 -*- 
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def ino(self,node,lst):
        if node == None:
            return
        self.ino(node.left,lst)
        lst.append(node.val)
        self.ino(node.right,lst)
        

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        #首先中序遍历得到树对应的序列，然后l和r分别指定头尾
        """
        lst = []
        self.ino(root,lst)
        l = 0
        r = len(lst) - 1
        while l < r:
            if lst[l] + lst[r] < k:
                l+=1
            elif lst[l] + lst[r] > k:
                r -= 1
            else:
                return True
        return False
            
