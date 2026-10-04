# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, value=0):
            nonlocal max_depth
            if node is None:
                return
            max_depth = max(max_depth, value + 1)
            dfs(node.left, value + 1)
            dfs(node.right, value + 1)
        
        max_depth = 0
        dfs(root, 0)
        return max_depth