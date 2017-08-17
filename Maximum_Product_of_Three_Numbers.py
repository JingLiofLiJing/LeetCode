# -*- coding:utf-8 -*-
'''
No.628
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        p1,p2,p3 = nums[-1],nums[-2],nums[-3]
        e1,e2 = nums[0],nums[1]
        re1 = p1*p2*p3
        re2 = e1*e2*p1
        if re1 > re2:
            return re1
        return re2

#   分析如下 p1,p2,p3：第一第二第三大的数字，e1e2第一小第二小的数字
#   ------------------------------   ---            p1p2p3       e1e2p1(小)
#   -----------------------------+   +--            p1p2p3（小） e1e2p1
#   ----------------------------++   +--            p1p2p3（小） e1e2p1
#   ---------------------------+++   +++            p1p2p3       e1e2p1  比较的大结果
# ...
#   --++++++++++++++++++++++++++++   --+            p1p2p3       e1e2p1  比较的大结果
#   -+++++++++++++++++++++++++++++   +++            p1p2p3       e1e2p1(小)
#   ++++++++++++++++++++++++++++++   +++            p1p2p3       e1e2p1(小)
#   无论哪种情况都是p1*p2*p3 和 e1*e2*p1的比较最大值，所以程序如上