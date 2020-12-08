class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = i - 1
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i-j], j * (i - j))

        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    S = Solution()
    print(S.integerBreak(n=10))
