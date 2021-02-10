class Solution:
    # 动态规划解法，dp[i][j]代表到达(i, j)的路径数目
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):

                # base case
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


if __name__ == "__main__":
    S = Solution()
    print(S.uniquePaths(m=7, n=3))
