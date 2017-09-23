# -*- coding: utf-8 -*-
'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.
'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        贪心算法：先对g和s需求进行排序，然后从后往前处理g和s，目的是为了让大的饼干优先满足大需求（即需求=饼干大小）的人，
        如果大饼干多了再去分给更小需求的人，直到饼干没了或者每个人都有饼干为止
        """
        g.sort()
        s.sort()
        i = len(g)-1
        j = len(s)-1
        while i>=0 and j>=0:
            if g[i] > s[j]:
                i -= 1
                continue
            i -= 1
            j -= 1
        return len(s) - 1 - j
        
