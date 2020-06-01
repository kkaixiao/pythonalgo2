"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where
each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then
this node's value is the smaller value among its two sub-nodes. More formally, the property
root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all
the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findSecondMinimumValue(self, root):
        if (root is None):
            return -1

        aList = []

        def inOrder(root):

            if root:
                inOrder(root.left)
                aList.append(root.val)
                inOrder(root.right)

        inOrder(root)

        res = list(set(aList))
        res.sort()
        if (len(res) >= 2):
            return res[1]
        return -1
