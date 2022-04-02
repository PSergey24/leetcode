from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(leftSide, rightSide):
            if not leftSide and not rightSide:
                return True

            if (not leftSide and rightSide) or (leftSide and not rightSide) or (
                    leftSide and rightSide and leftSide.val != rightSide.val):
                return False

            return dfs(leftSide.left, rightSide.right) and dfs(leftSide.right, rightSide.left)

        return dfs(root.left, root.right)
