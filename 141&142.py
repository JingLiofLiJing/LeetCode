# -*- coding: utf-8 -*- 
'''
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
          快慢指针方法：首先如果链表为空则不包含环，之后设置快慢指针的起始位置为根节点，然后如果快慢指针不一样，则快指针往前2步，慢指针往前1步，这样
        每次快慢指针比慢指针都多走一次，第n次走完快指针比满指针多n-1，如果快指针下一次或下下次为None，说明走到了尾部不含环
          假设满指针到了环的入口，环的长度为len，则快指针与慢指针的距离为0<=m<len(为len和为0同一种情况，则已经重合)，所以此时只需要再走m轮两者即可
        重合，此时慢指针肯定还没走完一圈。
          假设根节点到入口的长度为d，慢指针与快指针重合时离入口长度为m，剩下长度为n，环的长度为len，指针重合时走了慢指针走了S步，快指针走了2S步。
          S = d + m
          2S = d + m + c（多出圈数）*len
          m + n = len
          d + m = (c-1)*len + len
          d = (c-1)*len + (len-m)
          d = (c-1)*len + n
          可以知道节点到入口的长度等于环的若干倍数长度加上指针重合时距离环开始的长度
          所以此时一个节点在开头，一个节点在快慢指针重合的地方，同时每次往后面移动一格，则重合的地方为环开始的地方
        """
        if head == None:
            return False
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        find = None
        if head == None:
            return None
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                find = slow
                break
        if find == None:
            return None
        a = head
        b = find
        while a!= b:
            a = a.next
            b = b.next
        return a
