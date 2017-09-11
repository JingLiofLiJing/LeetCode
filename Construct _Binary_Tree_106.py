# -*- coding: utf-8 -*-
'''
No.106
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def haha(self,inorder,postorder,ino,pos,tn,lr,ino_start,ino_end,pos_start,pos_end):
        if ino_start <= ino_end:
            value = postorder[pos_end]
            ind = ino[value]
            t1 = t2 = None
            if lr == 1:
                tn.left = TreeNode(value)
                t1 = t2 = tn.left
            elif lr == 2:
                tn.right = TreeNode(value)
                t1 = t2 = tn.right
            chazhi = ind - ino_start
            if ino_start < ino_end:
                self.haha(inorder, postorder, ino, pos, t1, lr = 1, ino_start = ino_start, ino_end = ind - 1, pos_start = pos_start, pos_end = pos_start + chazhi - 1)
                self.haha(inorder, postorder, ino, pos, t2, lr = 1, ino_start = ind + 1, ino_end = ino_end, pos_start = pos_start + chazhi, pos_end = pos_end - 1)
        
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ino = {}
        pos = {}
        for i,j in enumerate(inorder):
            ino[j] = i
        for i,j in enumerate(postorder):
            pos[j] = i
        if inorder != []: 
            tnnn = TreeNode(postorder[-1])
            tn1 = tn2 = tnnn 
            ind = ino[tnnn.val]
            self.haha(inorder,postorder,ino,pos,tn1,1,0,ind-1,0,ind-1)
            self.haha(inorder,postorder,ino,pos,tn2,2,ind+1,len(inorder)-1,ind,len(inorder)-2)
            return tnnn
        else:
            return None
        
print  Solution().buildTree([4,6,2,7,5,1,3,9,8],[6,4,7,5,2,9,8,3,1])

