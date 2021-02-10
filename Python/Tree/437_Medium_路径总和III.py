from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 回溯法 超时 115/126
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #
    #     ans = []
    #
    #     def backtrack(root, value, trace):
    #         value += root.val
    #         if value == sum:
    #             ans.append(trace + [root.val])
    #         if root.left:
    #             backtrack(root.left, value, trace + [root.val])
    #         if root.right:
    #             backtrack(root.right, value, trace + [root.val])
    #
    #     if not root:
    #         return 0
    #     queue = deque([root])
    #
    #     while queue:
    #         start = queue.pop()
    #         if start.left:
    #             queue.append(start.left)
    #         if start.right:
    #             queue.append(start.right)
    #         backtrack(start, 0, [])
    #
    #     # print(ans)
    #     return len(ans)

    # 递归
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, prev):
            if not root:
                return 0

            prev = [num + root.val for num in prev]
            prev.append(root.val)
            count = 0
            for item in prev:
                if item == sum:
                    count += 1
            return count + dfs(root.left, prev) + dfs(root.right, prev)

        return dfs(root, [])


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
