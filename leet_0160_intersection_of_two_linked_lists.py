"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        cache = set()

        while headA:
            cache.add(headA)
            headA = headA.next

        while headB:
            if headB in cache:
                return headB
            headB = headB.next

        return None