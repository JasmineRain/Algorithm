class Solution:
    # 动态规划解法，dp[i][j]代表 s[i]到s[j]（包含两端）是否有效，状态转移由左下角元素得到，因此遍历从上至下，从左至右
    def longestValidParentheses(self, s: str) -> int:


if __name__ == "__main__":
    S = Solution()
    print(S.longestValidParentheses(s="()()(())"))
