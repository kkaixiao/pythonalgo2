"""
Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        l3 = ListNode(None)
        prev = l3

      # while both linked lists are not empty
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

      # once we reach end of a linked list, append the other
      # list because we know it is already sorted
        if l1 == None:
            prev.next = l2
        elif l2 == None:
            prev.next = l1
        return l3.next