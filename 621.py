# -*- coding: utf-8 -*- 
'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.
'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        nlogn方法：统计每个任务出现的次数从大到小排序，然后如果任务数量大于n的话每次选出前n+1个大的任务次数开始（对应任务次数-1），然后再次排序
        进行同样操作，知道任务数量小于等于n，这是则由最多任务数量-1再乘上n-1，再加上一共几个最多的任务（如果剩下任务数量不大于n，则至少也要进行
        最大数量个n+1循环）
        """
        tot = 0
        dict = {}
        for num in tasks:
            dict[num] = dict.get(num,0) + 1
        vs = dict.values()
        vs = sorted(vs, reverse=True)
        while(len(vs) > n):
            for i in range(n+1):
                vs[i] -= 1
            tot += (n+1)
            while 0 in vs:
                vs.remove(0)
            vs = sorted(vs, reverse=True)
        if len(vs) != 0:
            mx = max(vs)
            res = 0
            for mm in vs:
                if mm == mx:
                    res += 1
            tot = tot + (mx-1)*(n+1) + res
        return tot
