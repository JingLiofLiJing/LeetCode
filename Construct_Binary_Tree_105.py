# -*- coding: utf-8 -*- 
'''
No.105
Given preorder and inorder traversal of a tree, construct the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def haha(self, preorder,inorder,pre,ino,lr,tn,pre_start,pre_end,ino_start,ino_end):
        if ino_start <= ino_end:
            va = preorder[pre_start]
            ind = ino[va]
            chazhi = ino_end - ind
            t1 = t2 = None
            if lr == 1:
                tn.left = TreeNode(va)
                t1 = t2 = tn.left
            elif lr == 2:
                tn.right = TreeNode(va)
                t1 = t2 = tn.right
            if ino_start < ino_end:
                self.haha(preorder,inorder,pre,ino,1,t1,pre_start+1,pre_end-chazhi,ino_start,ind-1)
                self.haha(preorder,inorder,pre,ino,2,t2,pre_end-chazhi+1,pre_end,ind+1,ino_end)
        
    def buildTree(self, preorder,inorder):    
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        与中序后序题类似，前序第一个为根，然后按照chazhi的个数分开前序的左子树数组范围和右子树数组范围即可 
        """
        pre = ino = {}
        for i,j in enumerate(preorder):
            pre[j] = i
        for i,j in enumerate(inorder):
            ino[j] = i
        if preorder != []:
            va = preorder[0]
            ind = ino[va]
            tn = TreeNode(va)
            tn1 = tn2 = tn
            self.haha(preorder,inorder,pre,ino,1,tn1,1,ind,0,ind-1)
            self.haha(preorder,inorder,pre,ino,2,tn2,ind+1,len(preorder)-1,ind+1,len(preorder)-1)
            return tn
        else:
            return None
        
