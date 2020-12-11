class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        # 定义dp[i][j]为第i个到第j个字符是否为回文子串
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for i in range(len(s)):
            dp[i][i] = True

        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        # print(dp)
        return count


if __name__ == "__main__":
    S = Solution()
    print(S.countSubstrings(s="aaa"))
