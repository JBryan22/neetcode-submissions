# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.nodeCount: int = 0

        def dfs(root: TreeNode, highestPrev: int | float = -math.inf):
            if highestPrev <= root.val:
                self.nodeCount += 1
            highestPrev = max(highestPrev, root.val)

            if root.left:
                dfs(root.left, highestPrev)
            if root.right:
                dfs(root.right, highestPrev)
        
        dfs(root)
        return self.nodeCount
            