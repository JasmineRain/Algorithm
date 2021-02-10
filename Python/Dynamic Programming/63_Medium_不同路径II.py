from typing import List


class Solution:
    # 动态规划解法，dp[i][j]代表到达(i, j)的路径数目
    # 注意最佳判断策略  避免重复判断
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1
        for i in range(0, row):
            for j in range(0, col):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j]
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j-1]
        return dp[row - 1][col - 1]


if __name__ == "__main__":
    S = Solution()
    print(S.uniquePathsWithObstacles(obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]))
