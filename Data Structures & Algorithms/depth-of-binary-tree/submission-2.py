# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def do_dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth

        if root.left is not None:
            depth_left = self.do_dfs(root.left, depth + 1)
        else:
            depth_left = 0
        if root.right is not None:
            depth_right = self.do_dfs(root.right, depth + 1)
        else:
            depth_right = 0

        depth = max(depth_left, depth_right) + 1

        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return 0
        max_depth = self.do_dfs(root, max_depth)
        return max_depth