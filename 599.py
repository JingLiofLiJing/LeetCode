# -*- coding: utf-8 -*- 
'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        dict建立list1的<餐馆名，下标>队，然后如果list2出现了同样的餐馆，记录餐馆名和总下标和并计算出最小下标在输出即可
        """
        dict = {}
        minsum = len(list1)+len(list2)
        mindump = {}
        result = []
        for index,res in enumerate(list1):
            dict[res] = index
        for index,res in enumerate(list2):
            if res in dict:
                mindump[res] = dict[res] + index
                minsum = min(minsum,mindump[res])
        for k,v in mindump.items():
            if v == minsum:
                result.append(k)
        return result
