# -*- coding: utf-8 -*- 
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        首先判断空串和1的Z序列返回本身，其次对每一层i进行判断[0<=i<numRows],首先包含的元素为i以及交叉点下标kd-i，然后依次加上kd跨度并判断是否超界
        并添加到res中，时间复杂度o（n）
        """
        if s == "" or numRows == 1:
            return s
        res = ""
        length = len(s)
        kd = 2*(numRows - 1)
        for i in range(numRows):
            dd = []
            if i >= length:
                break
            dd.append(i)
            res += s[i] 
            if i + kd - 2*i < length and i + kd - 2*i != i and i + kd - 2*i != kd:
                dd.append(kd-i)
                res += s[kd-i]
            flag = 1
            while flag:
                for i in range(len(dd)):
                    sz = dd[i] + kd
                    if sz < length:
                        dd[i] = sz
                        res += s[sz]
                    else:
                        flag = 0
                        break
        return res
        
        
        def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        更好的方法：首先按照numRows建立每层深度的字符串数组res，遍历s每一个元素，放到index下标所对应的res字符串中，如果到了最底下，则
        step = -1表示往回走，到了开头（index=0）后step=1表示往下走，改变方向添加数组最后合并即可
        """
        if s == "" or numRows == 1:
            return s
        res = [""]*numRows
        index,step = 0,1
        for i in range(len(s)):
            res[index] += s[i]
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return "".join(res)
            
            
