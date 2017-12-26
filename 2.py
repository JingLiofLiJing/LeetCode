
# -*- coding: utf-8 -*- 
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their 
nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        判断是否为空然后保存进位就好
        """
        jinwei = 0
        head = res = None
        while l1 or l2:
            NM1 = NM2 = 0
            if l1:
                NM1 = l1.val
                l1 = l1.next
            if l2:
                NM2 = l2.val
                l2 = l2.next
            now = (jinwei + NM2 +NM1)%10
            jinwei = (jinwei + NM2 +NM1)/10
            print(now,jinwei)
            if not res:
                res = ListNode(now)
                head = res
            else:
                res.next = ListNode(now)
                res = res.next
        if jinwei:
            res.next = ListNode(jinwei)
        return head
            
