from typing import List


class Solution:
    # 动态规划解法，dp[i]代表到第i级阶梯的方法数
    # 注意状态图维度的选取
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


if __name__ == "__main__":
    S = Solution()
    print(S.climbStairs(n=2))
    # -2, 1, -3, 4, -1, 2, 1, -5, 4
