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
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return
    #
    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)
    #
    #     root.left, root.right = right, left
    #
    #     return root

    # 迭代法
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
