"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        some_head = ListNode(0)
        some_head.next = head
        node = some_head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return some_head.next