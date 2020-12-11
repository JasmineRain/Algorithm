from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0

        nrow = len(dungeon)
        ncol = len(dungeon[0])


if __name__ == "__main__":
    S = Solution()
    print(S.calculateMinimumHP(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
