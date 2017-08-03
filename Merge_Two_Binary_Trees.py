# -*- coding: utf-8 -*-
'''
No.617
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kuozhan(self,zuo,t1,t2):
        #传引用会改变指针，备份节点
        a1 = t1
        a2 = t2
        zuo2 = zuo
        if t1.left != None or t2.left != None:
            zuo.left = TreeNode(0)
            zuo = zuo.left
            if t1.left == None:
                t1.left = TreeNode(0)
            elif t2.left == None:
                t2.left = TreeNode(0)
            t1 = t1.left
            t2 = t2.left
            zuo.val = t2.val + t1.val
            self.kuozhan(zuo,t1,t2)
        if a1.right != None or a2.right != None:
            zuo2.right = TreeNode(0)
            zuo2 = zuo2.right
            if a1.right == None:
                a1.right = TreeNode(0)
            elif a2.right == None:
                a2.right = TreeNode(0)
            a1 = a1.right
            a2 = a2.right
            zuo2.val = a2.val + a1.val
            self.kuozhan(zuo2,a1,a2) 
        
                
    
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        zuo = TreeNode(t1.val+t2.val)
        tou = zuo
        self.kuozhan(zuo,t1,t2)
        return tou

a1 = TreeNode(1)
a2 = TreeNode(3) 
a3 = TreeNode(2)
a4 = TreeNode(5)

#a2.left = a4
a1.left = a2
a1.right = a3

b1 = TreeNode(2)
b2 = TreeNode(1)
b3 = TreeNode(3)
b4 = TreeNode(4)
b5 = TreeNode(7)

#b2.right = b4
b3.right = b5
b1.left = b2
b1.right = b3

res = Solution().mergeTrees(a1, b1)
print 'Done'















 
        