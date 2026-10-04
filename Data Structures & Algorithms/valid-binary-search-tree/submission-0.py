# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(node: Optional[TreeNode], min: int, max: int) -> bool:
            if node is None:
                return True
            if not (min < node.val < max):
                return False
            else:
                return DFS(node.left, min, node.val) and DFS(node.right, node.val, max)

        return DFS(root, -1000000000, 1000000000)
        