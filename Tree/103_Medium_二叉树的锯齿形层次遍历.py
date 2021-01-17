from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # BFS, then reverse the results
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     res = []
    #     if not root:
    #         return res
    #
    #     queue = deque([root])
    #     while queue:
    #         count = len(queue)
    #         temp = []
    #         while count > 0:
    #             node = queue.popleft()
    #             temp.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #             count -= 1
    #
    #         res.append(temp)
    #
    #     for seq, item in enumerate(res):
    #         if seq % 2 == 1:
    #             item.reverse()
    #     return res

    # BFS and reverse the result at the same time
    # direction == False means no need to reverse
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     res = []
    #     if not root:
    #         return res
    #
    #     queue = deque([root])
    #     direction = False
    #     while queue:
    #         count = len(queue)
    #         temp = []
    #         while count > 0:
    #             node = queue.popleft()
    #             temp.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #             count -= 1
    #         if direction:
    #             temp.reverse()
    #         res.append(temp)
    #         direction = not direction
    #     return res

    # DFS 递归
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        def dfs(root, level):
            if not root:
                return
            nonlocal res
            if level >= len(res):
                res.append([])
            if level % 2 == 1:
                res[level].insert(0, root.val)
            else:
                res[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return res