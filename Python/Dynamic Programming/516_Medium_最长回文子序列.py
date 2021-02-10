class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 定义dp[i][j]为第i个到第j个字符中，最长回文序列的长度
        if not s:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # print(dp)
        return dp[0][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.longestPalindromeSubseq(s="cbbd"))
