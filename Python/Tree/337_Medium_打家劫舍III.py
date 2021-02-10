from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 暴力递归法 超时123/124
    # def rob(self, root: TreeNode) -> int:
    #
    #     if not root:
    #         return 0
    #
    #     value = root.val
    #
    #     if root.left:
    #         value += (self.rob(root.left.left) + self.rob(root.left.right))
    #     if root.right:
    #         value += (self.rob(root.right.left) + self.rob(root.right.right))
    #
    #     return max(value, self.rob(root.left) + self.rob(root.right))

    # 动态规划递归
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return [0, 0]

            # 分别表示 不偷当前节点 和 偷当前节点  的利润
            res = [0, 0]

            left = _rob(root.left)
            right = _rob(root.right)

            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = left[0] + right[0] + root.val

            return res

        res = _rob(root)
        return max(res)

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
