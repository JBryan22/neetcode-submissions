# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        queue = deque([(root, 0)])
        prevDepth = -1
        while queue:
            node, depth = queue.popleft()

            if depth != prevDepth:
                res.append([node])
            else:
                res[depth].append(node)
            if node.left:
                queue.append(node.left)