# -*- coding: utf-8 -*- 
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        假设：该算法并没有遍历到容量最大的情况
        我们令容量最大时的指针为p_left和p_right。根据题设，我们可以假设遍历时左指针先到达p_left，但是当左指针为p_left时，右指针还没有经过p_right左指针就移动了
        已知当左指针停留在p_left时，它只有在两种场景下会发生改变

        左指针和右指针在p_left相遇，则右指针一定在前往p_left的途中经过p_right，与题设矛盾
        右指针位于p_right右侧且当前的值大于左指针。则在这种情况下，此时容器的盛水量比题设中最大的盛水量还要大，与题设矛盾
        因此该算法的遍历一定经过了最大的盛水量的情况
        """
        maxd = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            area = min(height[i],height[j])*(j-i)
            maxd = max(maxd,area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxd
