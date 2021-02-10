from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return
        stack = deque()
        node = root
        x = y = pre = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre and node.val < pre.val:
                y = node
                if x:
                    break
                else:
                    x = pre
            pre = node
            node = node.right

        x.val, y.val = y.val, x.val


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
