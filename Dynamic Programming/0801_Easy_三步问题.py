class Solution:
    def waysToStep(self, n: int) -> int:

        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + (dp[i-2] + dp[i-3]) % 1000000007) % 1000000007
        # print(dp)
        return dp[n]


if __name__ == "__main__":
    S = Solution()
    print(S.waysToStep(n=5))
