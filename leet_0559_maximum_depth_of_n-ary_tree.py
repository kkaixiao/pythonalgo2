
# embedded solution
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        heights = []
        def maxDepthCounter(node, depth):
            if not node.children:
                heights.append(depth)
                return

            for child in node.children:
                maxDepthCounter(child, depth + 1)

        maxDepthCounter(root, 1)
        return max(heights)


# two functions
class Solution:
    def __init__(self):
        self.heights = []

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        self.maxDepthCounter(root, 1)
        return max(self.heights)

    def maxDepthCounter(self, node, depth):
        if not node.children:
            self.heights.append(depth)
            return

        for child in node.children:
            self.maxDepthCounter(child, depth + 1)