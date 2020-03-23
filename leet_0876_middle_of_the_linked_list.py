"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        length = 0
        count_node = head

        while count_node != None:
            count_node = count_node.next
            length += 1

        middle_idx = (length // 2) + 1

        while middle_idx != 1:
            middle_idx -= 1
            head = head.next

        return head

    def middleNode2(self, head):

        slow_node = fast_node = head

        while fast_node and fast_node.next:

            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return slow_node