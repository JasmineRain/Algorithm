class Solution:
    # 动态规划解法，dp[i][j]代表 s[i]到s[j]（包含两端）是否为回文串，状态转移由左下角元素得到，因此遍历从上至下，从左至右
    def longestPalindrome_DynmicProgramming(self, s: str) -> str:

        size = len(s)
        if size < 2:
            return s
        max_length = 1
        start = 0
        dp = [[False for _ in range(size)] for _ in range(size)]
        for j in range(1, size):
            for i in range(0, j):

                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        start = i

        return s[start: start + max_length]

    # 中心扩散法，统一处理字符串长奇偶数情况
    def longestPalindrome_CenterSpreading(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        max_length = 1
        start = 0

    def _center_spread(self, s, start, end):
        


if __name__ == "__main__":
    S = Solution()
    print(S.longestPalindrome_DynmicProgramming(s="aaaa"))
