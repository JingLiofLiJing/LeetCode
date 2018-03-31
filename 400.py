'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        wei,xx = 1,9
        while n > xx:
            n -= xx
            wei += 1
            xx = 9*(10**(wei-1))*wei
        print(n,wei)
        a,b = n/wei,n%wei
        shuzi = 10**(wei-1) + a - 1
        if b:
            shuzi += 1
            return int(str(shuzi)[b-1])
        else:
            return shuzi%10
