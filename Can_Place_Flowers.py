#-*- coding:utf-8 -*-
'''
No.605
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #i和j为相近的放花的编号，两者之间的距离j-i满足放花的个数为（j-i）/2-1,计算总的最大可能放花数然后比较即可
        res = 0
        index = -1
        for ind,number in enumerate(flowerbed):
            if number == 1:
                #一串0为开始的判断（index = -1的情况），第一个为1的index减0除2来判断
                if index == -1:
                    res += ind/2
                else:
                    res += (ind - index)/2 -1
                index = ind
        #判断最后很多0结尾的情况，最后一位减掉最后一个index的长度除以2来判断
        #如果全是0的情况则为index == -1单独判断，如果index不为-1则另外判断
        if index == -1:
            res += ((len(flowerbed)+1)/2)
        else:
            res += (len(flowerbed) - index - 1)/2
        if res < n:
            return False
        return True
print Solution().canPlaceFlowers([0,0,1,0,0,0,0,1,0,0,0],4)
