# -*- coding: utf-8 -*- 
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

32位的符号整数范围是 -2147483648 ~ 2147483647

'''
def reverse1(x):
    """
    :type x: int
    :rtype: int
    12345
    """
    nums = [] 
    fushu = False
    if x == 0:
        return 0
    if x < 0:
        fushu = True
    zhengshu = abs(x)
    weishu = 10
    doushi0 = True   #不存高位的0
    while weishu >= 0:
        if weishu == 0:
            nums.append(zhengshu)
            break
        haha = zhengshu/(10**weishu)
        if haha > 0 and doushi0 == True:
            doushi0 = False 
        if doushi0 == False:
            nums.append(haha)
        zhengshu -=  haha * 10**weishu
        weishu -= 1
    lens = len(nums) - 1
    res = 0
    while lens >= 0:
        res += nums[lens]*(10**lens)
        lens -= 1
    if fushu:
        res = -res
    #不在范围里就返回0
    if res < (-2**31) or res > (2**31-1):
        return 0
    return res
    
print reverse1(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        