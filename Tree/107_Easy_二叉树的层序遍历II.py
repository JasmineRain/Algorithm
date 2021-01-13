from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # BFS 以空字符记录换层
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque()
        queue.append(root)
        queue.append("")
        order = []
        while queue and queue[0] != "":
            cur = queue.popleft()
            order.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

            if queue[0] == "":
                res.append(order.copy())
                order = []
                queue.append("")
                queue.popleft()
        res.reverse()
        return res

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
