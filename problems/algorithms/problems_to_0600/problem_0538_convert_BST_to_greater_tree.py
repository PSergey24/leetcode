from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        carry = 0

        def dfs(node):
            nonlocal carry
            if not node:
                return None

            dfs(node.right)
            carry += node.val
            node.val = carry
            dfs(node.left)
        dfs(root)
        return root
