# -*- coding: utf-8 -*- 
'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
'''
class MyCalendar(object):

    def __init__(self):
        self.dicts = {}
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        利用字典存储start，判断新来的start的大小，如果空直接添加，如果最大判断结尾，如果在重点判断前面结尾和后面开始
        由于使用字典，故时间效率低，超出limit
        """
        keys = self.dicts.keys()
        keys.sort()
        i = 0
        while i < len(keys):
            if start == keys[i]:
                return False
            elif start < keys[i]:
                break
            i += 1
        if self.dicts == {} or ( i == 0 and end<= keys[i] ) or (i == len(keys) and start >= self.dicts[keys[-1]]) or (start >= self.dicts[keys[i-1]] and end <= keys[i]):
            self.dicts[start] = end
            return True
        return False
##############################################################################################################
class Node:
    def __init__(self,s,e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None
        
class MyCalendar(object):

    def __init__(self):
        self.root = None
        
    def gaoshi(self,node,s,e):
        if s >= node.e:
            if node.right:
                return self.gaoshi(node.right,s,e)
            else:
                node.right = Node(s,e)
                return True
        elif e <= node.s:
            if node.left:
                return self.gaoshi(node.left,s,e)
            else:
                node.left = Node(s,e)
                return True
        return False
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        #采用树结构来进行存储，查找效率为logn，所以时间不会溢出
        """
        if not self.root:
            self.root = Node(start,end)
            return True
        else:
            return self.gaoshi(self.root,start,end)
