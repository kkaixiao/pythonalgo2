"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        curr = head
        carry, tmp1, tmp2 = 0, l1, l2

        while tmp1 or tmp2:

            if tmp1:
                d1 = tmp1.val
            else:
                d1 = 0

            if tmp2:
                d2 = tmp2.val
            else:
                d2 = 0

            sum = d1 + d2 + carry

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if tmp1 != None:
                tmp1 = tmp1.next

            if tmp2 != None:
                tmp2 = tmp2.next

        if carry > 0:
            curr.next = ListNode(1)

        return head.next
