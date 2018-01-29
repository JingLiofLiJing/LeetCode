# -*- coding: utf-8 -*- 
'''
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.
Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
'''
class MyCalendarTwo:
    def __init__(self):
        #重复的范围集合（如果再次出现在此则返回false）
        self.overlaps = []
        #第一次出现的范围集合
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
