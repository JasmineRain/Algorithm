from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def backtrack(start, end):
            if start > end:
                return [None, ]
            ans = []
            for i in range(start, end + 1):

                left = backtrack(start, i - 1)
                right = backtrack(i + 1, end)

                for l in left:
                    for r in right:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        ans.append(cur)
            return ans

        return backtrack(1, n)


if __name__ == "__main__":
    S = Solution()
    print(S.generateTrees(n=3))
