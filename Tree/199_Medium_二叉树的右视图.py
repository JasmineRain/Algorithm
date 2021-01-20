from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # BFS
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if not root:
    #         return res
    #
    #     queue = deque([root])
    #     while queue:
    #         count = len(queue)
    #         while count > 0:
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #             count -= 1
    #
    #         res.append(node.val)
    #     return res

    # DFS
    def rightSideView(self, root: TreeNode) -> List[int]:

        res = []

        def dfs(root, depth):
            if not root:
                return

            if depth == len(res):
                res.append(root.val)

            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return res