class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nrow = len(p) + 1
        ncol = len(s) + 1

        # 定义dp[i][j]为p的前i个元素是否能匹配s的前j个元素
        dp = [[False for _ in range(ncol)] for _ in range(nrow)]

        dp[0][0] = True
        for i in range(1, nrow):
            dp[i][0] = dp[i-1][0] and p[i-1] == "*"

        for i in range(1, nrow):
            for j in range(1, ncol):
                if s[j-1] == p[i-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i-1] == "*":
                        dp[i][j] = any(dp[i-1][0:j + 1])
                    else:
                        dp[i][j] = False
        # for i in range(nrow):
        #     print(dp[i])
        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.isMatch(s="adceb", p="*a*b"))
