"""
Given two binary trees and imagine that when you put one of them to cover the other, some
nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the NOT null node
will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # stuck somewhere, fairly stupid and slow method
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1:
            if t2:
                t1.val = t1.val + t2.val
            else:
                t2 = TreeNode()
                t1.val = t1.val
        else:
            if t2:
                t1 = TreeNode()
                t1.val = t2.val
            else:
                return t1

        if t1.left and t2.left:
            self.mergeTrees(t1.left, t2.left)
        elif t1.left and not t2.left:
            t2.left = TreeNode()
            self.mergeTrees(t1.left, t2.left)
        elif not t1.left and t2.left:
            t1.left = TreeNode()
            self.mergeTrees(t1.left, t2.left)

        if t1.right and t2.right:
            self.mergeTrees(t1.right, t2.right)
        elif t1.right and not t2.right:
            t2.right = TreeNode()
            self.mergeTrees(t1.right, t2.right)
        elif not t1.right and t2.right:
            t1.right = TreeNode()
            self.mergeTrees(t1.right, t2.right)

        return t1


    # found out what's problem in the previous answer
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        if t1 and t2:
            t1.val = t1.val + t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
