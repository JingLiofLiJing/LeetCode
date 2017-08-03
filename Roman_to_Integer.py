# -*- coding: utf-8 -*- 
'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.


基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目、都不能超过三个；放在大数的左边只能用一个；
不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目、只能使用一个；

I V X  L  C   D   M
1 5 10 50 100 500 1000


M MM MMM 
C CC CCC CD  D DC DCC DCCC CM 
X XX XXX XL L LX LXX LXXX XC 
I II III IV V VI VII VIII IX 

dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
MCMLXXVI 1976

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            if s[i] == "M":
                count = 1
                i += 1
                while i < len(s) and s[i] == "M":
                    count += 1
                    i += 1
                result += count * 1000
                continue
            if s[i] == 'C':
                i += 1
                if i < len(s) and s[i] == "M":
                    result += 900
                    i += 1
                elif i < len(s) and s[i] == "D":
                    result += 400
                    i += 1
                else:
                    count = 1
                    while i < len(s) and s[i] == "C":
                        count += 1
                        i += 1
                    result += 100 * count
                continue
            if s[i] == "D":
                i += 1
                count = 0
                while i < len(s) and s[i] == "C":
                    i += 1
                    count += 1
                result = result + 500 +count*100
                continue
            if s[i] == "X":
                i += 1
                if i < len(s) and s[i] == "C":
                    result += 90
                    i += 1
                elif i < len(s) and s[i] == "L":
                    result += 40
                    i += 1
                else:
                    count = 1
                    while i < len(s) and s[i] == "X":
                        count += 1
                        i += 1
                    result += 10 * count
                continue
            if s[i] == "L":
                i += 1
                count = 0
                while i < len(s) and s[i] == "X":
                    count += 1
                    i += 1
                result = result + 50 +count*10
                continue
            if s[i] == "V":
                i += 1
                count = 0
                while i < len(s) and s[i] == "I":
                    i += 1
                    count += 1
                result = result + 5 +count
                continue
            if s[i] == "I":
                i += 1
                if i < len(s) and s[i] == "X":
                    result += 9
                    i += 1
                elif i < len(s) and s[i] == "V":
                    result += 4
                    i += 1
                else:
                    count = 1
                    while i < len(s) and s[i] == "I":
                        count += 1
                        i += 1
                    result += count
            continue
        return result
                
        


print Solution().romanToInt("MCMLXXXIV")

