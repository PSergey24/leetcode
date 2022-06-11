from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # dfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.small = float('inf')
        def dfs(node, num):
            if not node:
                return

            if not node.left and not node.right:
                self.small = min(self.small, num)

            dfs(node.left, num + 1)
            dfs(node.right, num + 1)

        dfs(root, 1)
        return self.small

    # bfs
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            cand, num = q.popleft()
            if not cand.left and not cand.right:
                return num
            if cand.left:
                q.append((cand.left, num + 1))
            if cand.right:
                q.append((cand.right, num + 1))
        return -1
