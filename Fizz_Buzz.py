# -*- coding: utf-8 -*-
'''
No.412
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both 
three and five output “FizzBuzz”.
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_list = []
        for i in range(1,n+1):
            if i%3 == 0 and i %5 == 0:
                ret_list.append("FizzBuzz")
            elif i%3 == 0:
                ret_list.append("Fizz")
            elif i%5 == 0:
                ret_list.append("Buzz")
            else:
                ret_list.append("%s"%i)
        return ret_list