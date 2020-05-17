"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all
of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def checkVal(s1, t1):
            if not s1 and not t1:
                return True
            if s1 and not t1 or t1 and not s1:
                return False
            if s1.val != t1.val:
                return False
            return checkVal(s1.left, t1.left) and checkVal(s1.right, t1.right)

        if not s:
            return False
        if s.val == t.val and checkVal(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)