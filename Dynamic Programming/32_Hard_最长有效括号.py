class Solution:
    # 动态规划解法，dp[i][j]代表 s[i]到s[j]（包含两端）是否有效，状态转移由左下角元素得到，因此遍历从上至下，从左至右
    def longestValidParentheses(self, s: str) -> int:

        # definition
        size = len(s)
        if size < 2:
            return 0
        max_length = 0
        start = 0
        dp = [0 for _ in range(size)]
        # iteration
        for i in range(0, size):
            # base case
            if i == 0 or s[i] == "(":
                dp[i] = 0
            # s[i] == ")"
            else:
                if s[i-1] == "(":
                    dp[i] = 2
                    if i - 2 > 0:
                        dp[i] += dp[i-2]
                # s[i-1] == ")",  s is like "_____))"
                else:
                    if i - 1 - dp[i-1] >= 0 and s[i-1-dp[i-1]] == "(":
                        dp[i] = dp[i-1] + 2
                        if i - 2 - dp[i-1] > 0:
                            dp[i] += dp[i-2-dp[i-1]]

            if dp[i]:
                max_length = dp[i] if dp[i] > max_length else max_length
        return max_length


if __name__ == "__main__":
    S = Solution()
    print(S.longestValidParentheses(s="(())"))
