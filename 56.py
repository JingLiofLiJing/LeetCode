# -*- coding: utf-8 -*- 
'''
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        #首先判断一下是否为空防止start和end输出[0,0],然后按照每个数据结构的start字段来进行排序，再依次判断后面的start如果小于end则两者有交集
        如果end大的话更新end。如果当前的范围和之前的start,end没有交集则记录之前的范围记录再更新新的范围前后即可
        """
        if intervals == []:
            return []
        res = []
        start = end = 0
        intervals = sorted(intervals,key = lambda d:d.start)
        for i in range(len(intervals)):
            if i == 0:
                start,end = intervals[i].start,intervals[i].end
            elif intervals[i].start <= end:
                if intervals[i].end > end:
                    end = intervals[i].end
            elif intervals[i].start > end: 
                res.append([start,end])
                start,end = intervals[i].start,intervals[i].end
        #最后一次的范围要加到结果里面
        res.append([start,end])
        return res
