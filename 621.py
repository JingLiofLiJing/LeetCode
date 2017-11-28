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
    
    
        
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        更好的方法o（n）：考虑出现频率最高的元素假设是A，假设A的出现次数为x，则要满足要求，A之间的空缺的槽为（x-1）个，并且每个槽的大小为n个
        所以至少的位置为（x-1）*（n+1）+1，但是一般情况下最高次数的任务不可能总是只有A一个，可能有k个，则如果要满足这些最高次数的任务的调度，则
        有序排列在每个A的槽后面即可，就算槽的个数大了或者小了都可以，则这样会产生两个结果（只考虑最大频数的任务ABC...）：
            1 槽的数量小于 k-1，则照样排列在后面，超出的也接在后面，则照样满足要求，此时会发现中间没有空缺的槽，则其实最大长度也就是这些任务总的
            数量，同时第频数的任务也是如此
            2 槽的数量大于等于k-1，则直接按顺序把剩下的任务排在槽里就行了，这样的最大时间调度为（x-1）*（n+1）+k个
            所以综合上述情况，去max（序列长度，（x-1）*（n+1）+k即可满足要求）
        """
        tot = 0
        dict = {}
        for num in tasks:
            dict[num] = dict.get(num,0) + 1
        vs = dict.values()
        vs = sorted(vs, reverse=True)
        mx = max(vs)
        num = vs.count(mx)
        return max(len(tasks),(n+1)*(mx-1)+num)
