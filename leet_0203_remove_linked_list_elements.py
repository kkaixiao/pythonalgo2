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


    def removeElements_rec1(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        # print(head, head.next)
        head.next = self.removeElements(head.next, val)
        print(head.val)
        # return head
        # print(head.next)
        # return head if head.val != val else head.next
"""
    ListNode
    {val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: None}}}
    ListNode
    {val: 2, next: ListNode{val: 6, next: None}}
    
    ListNode
    {val: 2, next: ListNode{val: 6, next: None}}
    ListNode
    {val: 6, next: None}
    
    ListNode
    {val: 6, next: None}
    None
"""