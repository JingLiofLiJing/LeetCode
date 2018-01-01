
# -*- coding: utf-8 -*- 
'''
Reverse a singly linked list.
click to show more hints.
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #记录初始节点并将其next置为None，然后bc分别记录a.next，a.next.next，让b.next = a，因为b的next往回指了，所以当b不为None时记录C
        否则返回a即可
        a = head
        if a!= None:
            b = a.next
            a.next = None
            while b != None:
                c = b.next
                b.next = a
                a = b
                b = c
        return a
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归方法:除开每次头节点将后面第一个节点带入递归函数求反过来的开头，然后头结点的下一个的下一个指向自己，再讲自己的下一个为None即可
        """
        #head为None判断考虑空链表情况
        if head == None or head.next == None:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        
    
