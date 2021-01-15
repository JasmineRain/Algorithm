from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归法，利用后序遍历
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root or root.val == p.val or root.val == q.val:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #
    #     if not left:
    #         return right
    #     if not right:
    #         return left
    #
    #     return root

    # 非递归法
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(root, target):
            temp = []
            node = root
            pre = None
            while node or temp:
                while node:
                    temp.append(node)
                    if node.val == target.val:
                        path = [item.val for item in temp]
                        return temp, path
                    node = node.left

                node = temp.pop()
                if not node.right or node.right == pre:
                    pre = node
                    node = None
                else:
                    temp.append(node)
                    node = node.right

        track1, path1 = findPath(root, p)
        # print(path1)
        track2, path2 = findPath(root, q)
        # print(path2)

        for i in range(min(len(track1), len(track2))):
            if track1[i] != track2[i]:
                return track1[i - 1]
        return track1[min(len(track1), len(track2)) - 1]

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
