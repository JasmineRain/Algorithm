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
    # def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    #
    #     if not t1:
    #         return t2
    #     if not t2:
    #         return t1
    #
    #     root = TreeNode(t1.val + t2.val)
    #     root.left = self.mergeTrees(t1.left, t2.left)
    #     root.right = self.mergeTrees(t1.right, t2.right)
    #     return root

    # 迭代法
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        queue = deque()
        queue.append([t1, t2])
        while queue:
            n1, n2 = queue.popleft()
            n1.val += n2.val
            if n1.left and n2.left:
                queue.append([n1.left, n2.left])
            elif not n1.left:
                n1.left = n2.left
            # n1左不空，n2左空的情况无需操作

            if n1.right and n2.right:
                queue.append([n1.right, n2.right])
            elif not n1.right:
                n1.right = n2.right

        return t1


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
