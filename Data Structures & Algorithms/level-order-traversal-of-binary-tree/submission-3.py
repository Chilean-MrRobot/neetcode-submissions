# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(queue: Optional[TreeNode], levels: List[int]) -> None:
            while queue:
                node = queue.popleft()
                level = levels.pop(0)
                #DS
                if len(list_vals) == level:
                    list_vals.append([])
                list_vals[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                    levels.append(level+1)
                if node.right:
                    queue.append(node.right)
                    levels.append(level+1)
            return

        list_vals = []
        if root is None:
            return []
        queue = deque([root])
        levels = [0]
        BFS(queue, levels)
        return list_vals