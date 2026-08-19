# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        returnDepth = []
        if root == None:
            return returnDepth

        def iterateRecursive(node: TreeNode, depth: int, returnDepth: List[List[int]]) -> List[List[int]]:
            # This Step
            if len(returnDepth) == depth:
                returnDepth.append([])
            #print(depth, node.val)

            returnDepth[depth].append(node.val)
            # Level Left
            if node.left != None:
                depth, returnDepth = iterateRecursive(node.left, depth+1, returnDepth)
                depth -= 1
            # Level Rights
            if node.right != None:
                depth, returnDepth = iterateRecursive(node.right, depth+1, returnDepth)
                depth -= 1
            return depth, returnDepth

        depth, returnDepth = iterateRecursive(root, 0, returnDepth)
        #print(depth, returnDepth)
        return returnDepth
            
        