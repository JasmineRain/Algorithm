from collections import Counter
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return

        return self.merge(buildings, 0, len(buildings) - 1)

    def merge(self, lists, left, right):
        if left == right:
            return [[lists[left][0], lists[left][2]], [lists[left][1], 0]]
        idx = left + (right - left) // 2
        l1 = self.merge(lists, left, idx)
        l2 = self.merge(lists, idx + 1, right)
        return self.merge_two_lists(l1, l2)

    def merge_two_lists(self, l1, l2):
        i, j = 0, 0
        res = []
        h1, h2 = 0, 0
        while i < len(l1) or j < len(l2):
            x1 = float("inf") if i >= len(l1) else l1[i][0]
            x2 = float("inf") if j >= len(l2) else l2[j][0]
            add_x = 0
            if x1 < x2:
                add_x = x1
                h1 = l1[i][1]
                i += 1
            elif x1 > x2:
                add_x = x2
                h2 = l2[j][1]
                j += 1
            else:
                add_x = x1
                h1, h2 = l1[i][1], l2[j][1]
                j += 1
                i += 1

            add_h = max(h1, h2)
            if not res or add_h != res[-1][1]:
                res.append([add_x, add_h])

        return res


if __name__ == "__main__":
    S = Solution()
    print(S.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    print(S.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
