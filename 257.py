'''
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def haha(self,node,lst,res):
        lst.append(node.val)
        if not node.left and not node.right:
            if len(lst) > 1:
                xx = reduce(lambda x,y:str(x)+"->"+str(y),lst)
            else:
                xx = str(lst[0])
            res.append(xx)
        else:
            if node.left:
                self.haha(node.left,lst,res)
            if node.right:
                self.haha(node.right,lst,res)
        lst.pop()
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root:
            lst = []
            self.haha(root,lst,res)
        return res       
