from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # BFS
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     ans = 1
    #     queue = deque([root])
    #     while queue:
    #         size = len(queue)
    #         while size > 0:
    #             node = queue.popleft()
    #             size -= 1
    #             if not node.left and not node.right:
    #                 return ans
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         ans += 1
    #     return ans

    # DFS
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        ans = float("inf")

        def dfs(root, level):
            if not root:
                return
            nonlocal ans
            if not root.left and not root.right:
                ans = min(ans, level + 1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return ans

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
