# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        k_value = 0

        def DFS(node: Optional[TreeNode]) -> None:
            nonlocal counter, k_value

            if node is None:
                return
            
            DFS(node.left)
            counter += 1
            if counter == k:
                k_value = node.val
            DFS(node.right)
            return

        DFS(root)

        return k_value