# -*- coding: utf-8 -*-
'''
No.637
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        start = [root]
        while start != []:
            opt = []
            temp = 0
            for node in start:
                temp += node.val
                if node.left != None:
                    opt.append(node.left)
                if node.right != None:
                    opt.append(node.right)
            if temp%len(start) == 0:
                res.append(temp/len(start))
            else:
                res.append(float(temp)/len(start))
            start = opt
        return res
    
    
    def av2(self, root):
        info = []
        res = []
        def dfs(node,depth):
            if node == None:
                return
            if len(info) < depth:
                info.append([0,0])
            info[depth-1][0] += node.val
            info[depth-1][1] += 1
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        #从第一层递归往下建立
        dfs(root,1)
        for a,b in info:
            if a%b == 0 :
                res.append(a/b)
            else:
                res.append(float(a)/b)
        return res

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
 
a.left = b
a.right = c 
c.left = d
c.right = e

print Solution().av2(a)