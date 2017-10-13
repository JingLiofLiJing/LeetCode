#-*- coding:utf-8 -*-
'''
No.387
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        字典存放对应数字的下标，长度为次数，长度大于1的第一个输出，时间复杂度o（n）
        """
        cs = {}
        for index,num in enumerate(s):
            cs.setdefault(num,[])
            cs[num].append(index)
        for num in s:
            if len(cs[num]) == 1:
                return cs[num][0]
        return -1
        
      
     def firstUniqChar2(self, s):
      """
      :type s: str
      :rtype: int
      set(s)过滤重复数字，然后每个数字从两头找第一个出现的，如果两头找的下标一样则只出现一次，将下标加入indexs中，处理完后返回indexs中最小值
      """
      indexs = []
      for num in set(s):
          if s.find(num) == s.rfind(num):
              indexs.append(s.index(num))
      if indexs:   
          return min(indexs) 
      else:
          return -1
        
     
