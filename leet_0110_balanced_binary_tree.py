# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Height:
    def __init__(self):
        self.height = 0


class Solution:

    # function to check if tree is height-balanced or not
    def isBalanced(self, root):

        # Base condition
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)


        if (abs(left_height - right_height) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False


    def height(self, root):

        # base condition when binary tree is empty
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1