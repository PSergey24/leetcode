from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = []

        def helper(root):
            if root:
                self.res.insert(0, root.val)
                helper(root.right)
                helper(root.left)

        helper(root)
        return self.res
