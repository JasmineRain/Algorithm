class Solution:
    def numTrees(self, n):

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]


if __name__ == "__main__":
    S = Solution()
    print(S.numTrees(n=20))
