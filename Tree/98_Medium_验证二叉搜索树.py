from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归法
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(root, min, max):
    #         if not root:
    #             return True
    #
    #         if root.val >= max or root.val <= min:
    #             return False
    #         if not dfs(root.left, min, root.val):
    #             return False
    #         if not dfs(root.right, root.val, max):
    #             return False
    #         return True
    #
    #     return dfs(root, -float("inf"), float("inf"))

    # 迭代法 使用中序遍历，中序遍历平衡二叉树，输出的序列必是递增序列
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = - float("inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right

        return True


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
