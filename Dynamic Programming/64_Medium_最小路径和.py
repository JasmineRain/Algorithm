from typing import List


class Solution:
    # 动态规划解法，dp[i][j]代表到达(i, j)的路径数目
    # 注意最佳判断策略  避免重复判断
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif i != 0 and j != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[row - 1][col - 1]


if __name__ == "__main__":
    S = Solution()
    print(S.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
