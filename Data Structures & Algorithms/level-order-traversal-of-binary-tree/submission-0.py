# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([(root, 0)])
        prevDepth = -1
        while queue:
            node, depth = queue.popleft()

            if depth > prevDepth:
                res.append([node.val])
                prevDepth = depth
            else:
                res[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
        return res