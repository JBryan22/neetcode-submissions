# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount: int = 0
        highestPrev: int | float = -math.inf

        stack = [(root, highestPrev)]

        while stack:
            node, highestPrev = stack.pop()

            if highestPrev <= node.val:
                goodCount += 1
            
            highestPrev = max(highestPrev, node.val)

            if node.left:
                stack.append((node.left, highestPrev))
            if node.right:
                stack.append((node.right, highestPrev))

        return goodCount