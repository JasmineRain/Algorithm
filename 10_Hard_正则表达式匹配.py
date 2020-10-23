class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s and len(p) == 1:
            return False

        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for r in range(nrow)]

        # base case
        dp[0][0] = True
        dp[0][1] = False
        for j in range(2, ncol):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == ".":
                    dp[r][c] = dp[r-1][c-1]
                elif p[j] == "*":
                    if p[j-1] == s[i] or p[j-1] == ".":
                        dp[r][c] = dp[r][c-2] or dp[r-1][c]
                    else:
                        dp[r][c] = dp[r][c-2]
                else:
                    dp[r][c] = False
        return dp[len(s)][len(p)]


if __name__ == "__main__":
    S = Solution()
    print(S.isMatch(s="mississippi", p="mis*is*p*."))



