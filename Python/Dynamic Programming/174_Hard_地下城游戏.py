from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0

        nrow = len(dungeon)
        ncol = len(dungeon[0])

        # 定义dp[i][j]为从(i, j)到达右下角所需要的最低HP
        dp = [[1 for _ in range(ncol)] for _ in range(nrow)]
        dp[-1][-1] = max(1, - dungeon[-1][-1] + 1)

        for i in range(nrow - 1, -1, -1):
            for j in range(ncol - 1, -1, -1):
                if i == nrow - 1 and j == ncol - 1:
                    dp[i][j] = max(1, - dungeon[-1][-1] + 1)
                elif i == nrow - 1:
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                elif j == ncol - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        # for i in range(0, nrow):
        #     print(dp[i])
        return dp[0][0]


if __name__ == "__main__":
    S = Solution()
    print(S.calculateMinimumHP(dungeon=[[-2, -3, 3],
                                        [-5, -10, 1],
                                        [10, 30, -5]]))
