# -*- coding: utf-8 -*- 
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        #分别建立p的字典和遍历s下的同长度字典，每次遍历时删去最后一个添加目前下标的新元素然后不断做比较即可O(n)
        """
        if s == "" or len(s) < len(p):
            return []
        res = []
        dicp = {}
        dics = {}
        i = 0
        for v in p:
            dicp[v] = dicp.get(v,0)+1
        for i in range(len(s)):
            if i < len(p):
                dics[s[i]] = dics.get(s[i],0)+1
                if i == len(p) - 1:
                    if dicp == dics:
                        res.append(i - len(p)+1)
            else:
                j = i - len(p)
                dics[s[j]] -= 1
                if dics[s[j]] == 0:
                    dics.pop(s[j])
                dics[s[i]] = dics.get(s[i],0)+1
                if dicp == dics:
                    res.append(i - len(p)+1)                
        return res
        
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        于上述方法类似，滑动窗口的方法，dict首先记录p的出现次数，然后l和r表示截取的区间，如果当前r的次数大于1，count-=1表示包含了此元素，
        同时如r-l=p长度（r每次匹配完都会往后移一位），则移动l保证截取长度相同，同时如果dict[s[l]] >= 0，说明移动时空出了此需要的元素，count
        加1表示需要后面再来一个同样元素进行填补，count=0表示所有的元素都得到了填补，则加入res即可，少了一个dict的构建。
        """
        if s == "" or len(s) < len(p):
            return []
        res = []
        dict = {}
        count = len(p)
        l = r = 0
        for v in p:
            dict[v] = dict.get(v,0)+1
        while r < len(s):
            if dict.get(s[r],0) >= 1:
                count -= 1
            dict[s[r]] = dict.get(s[r],0) - 1
            r += 1
            if count == 0:
                res.append(l)
            if r - l == len(p) and dict[s[l]] >= 0:
                count += 1
            if r - l == len(p):
                dict[s[l]] += 1
                l += 1
        return res
        
        
        
    
