"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursion
class Solution(object):
    def swapPairs(self, head):
        if not head or (head and not head.next):
            return head

        tmp = head.next

        head.next = self.swapPairs(head.next.next)

        tmp.next = head

        return tmp


# iteration
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        temp = head
        head = head.next
        while True:

            if not temp or not temp.next:
                break

            temp2 = temp.next.next
            temp.next.next = temp
            # if no. of nodes are even
            if not temp2:
                temp.next = None
            # if no. of nodes are odd
            elif not temp2.next:
                temp.next = temp2

            else:
                temp.next = temp2.next
            temp = temp2

        return head