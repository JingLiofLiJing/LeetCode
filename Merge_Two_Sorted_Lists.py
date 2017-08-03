# -*- coding: utf-8 -*- 
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_list = None  #保存开头节点 
        first = True       #判断是否开头
        kaitou = None      #建立节点
        # 如果其中一个为None
        if l1 == None and l2 != None:
            kaitou = l2
            start_list = kaitou
            l2 = l2.next
        elif l2 == None and l1 != None:
            kaitou = l1
            start_list = kaitou
            l1 = l1.next
        #建立链表
        while l1!=None and l2!=None:
            if l1.val <= l2.val:
                if first == True:
                    kaitou = l1
                    start_list = kaitou
                    first = False
                else:
                    kaitou.next = l1
                    kaitou = kaitou.next
                l1 = l1.next
            elif l2.val < l1.val:
                if first == True:
                    kaitou = l2
                    start_list = kaitou
                    first = False
                else:
                    kaitou.next = l2
                    kaitou = kaitou.next
                l2 = l2.next
        if l1 == None:
            while l2 != None:
                kaitou.next = l2
                kaitou = kaitou.next
                l2 = l2.next
        elif l2 == None:
            while l1 != None:
                kaitou.next = l1
                kaitou = kaitou.next
                l1 = l1.next
        return start_list
    
    