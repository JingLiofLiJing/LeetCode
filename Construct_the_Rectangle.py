# -*- coding: utf-8 -*- 
'''
No.492
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, 
whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
'''
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        #最好的情况就是可以开平方，这样差值为0，如果不行，则从开平方取整向下找，找到的第一个即为差值最小的数（小的那个）
                        然后添加即可
        """
        a = int(area**.5)
        while a>=1:
            if area%a == 0:
                return [area/a,a]
            a -= 1
