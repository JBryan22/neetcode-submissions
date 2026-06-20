# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        last_visited = None
        depths = {}
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            peek_top = stack[-1]
            if peek_top.right and peek_top.right != last_visited:
                curr = peek_top.right
            else:
                node = stack.pop()

                left_h = depths.get(node.left, 0)
                right_h = depths.get(node.right, 0)

                if abs(left_h - right_h) > 1:
                    return False

                depths[node] = 1 + max(left_h, right_h)
                last_visited = node
        return True
