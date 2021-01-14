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
    # def maxDepth(self, root: TreeNode) -> int:
    #
    #     if not root:
    #         return 0
    #
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                size -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
