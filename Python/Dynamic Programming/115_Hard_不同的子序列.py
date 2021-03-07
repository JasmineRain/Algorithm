class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 定义dp[i][j]为t的前i个字符能被s的前j个字符组成的次数
        if len(s) < len(t):
            return 0
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(t) + 1):
            dp[i][0] = 0

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.numDistinct(s="rabbbit", t="rabbit"))
    print(S.numDistinct(s="babgbag", t="bag"))
