# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def BFS(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while cola:
                node = cola.popleft()
                # DS
                dummy = node.left
                node.left = node.right
                node.right = dummy
                if node.left:
                    cola.append(node.left)
                if node.right:
                    cola.append(node.right)
            return

        if root is None:
            return None
        cola = deque([root])
        BFS(cola)
        return root