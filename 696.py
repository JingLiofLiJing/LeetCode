# -*- coding: utf-8 -*- 
'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        b表示前1个连续组的长度，a表示现在所在连续组的长度，a<=b则满足条件，当遇到分歧点时，a更新b，在比较一次，这一次res肯定+1
        """
        res = b = a = i = 0
        while i < len(s):
            if i == 0 or s[i] == s[i-1]:
                a += 1
            else:
                b = a
                a = 1
            if a <= b:
                res += 1
            i += 1        
        return res
        
    def countBinarySubstrings(self, s):
        #把0和1间隔分开，然后变成长度数组，数组之间交叉比对即可
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        lst = list(s)
        return sum([min(a,b) for a,b in zip(lst[:-1],lst[1:])])
        
        
        
            
