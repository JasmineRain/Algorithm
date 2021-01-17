# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 中序遍历递归法1
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     res = []
    #
    #     def inorder(root):
    #         if not root:
    #             return
    #         inorder(root.left)
    #         res.append(root.val)
    #         inorder(root.right)
    #
    #     inorder(root)
    #     return res[k-1]

    # 中序遍历递归法2, early stop
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     res = []
    #
    #     def inorder(root):
    #         if not root or len(res) == k:
    #             return
    #         inorder(root.left)
    #         if len(res) == k:
    #             return
    #         res.append(root.val)
    #         inorder(root.right)
    #
    #     inorder(root)
    #     return res[-1]

    # 中序遍历非递归法
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        if not root:
            return
        stack = deque()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res = node.val
            k -= 1
            if k == 0:
                return res
            node = node.right
