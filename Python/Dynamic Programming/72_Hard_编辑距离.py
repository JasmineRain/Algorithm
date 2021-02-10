class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nrow = len(word1) + 1
        ncol = len(word2) + 1
        dp = [[0 for c in range(ncol)] for r in range(nrow)]

        for i in range(0, nrow):
            dp[i][0] = i
        for j in range(0, ncol):
            dp[0][j] = j

        for i in range(1, nrow):
            for j in range(1, ncol):
                left = dp[i][j-1] + 1
                top = dp[i-1][j] + 1
                tl = dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1] + 1
                dp[i][j] = min(left, top, tl)

        return dp[len(word1)][len(word2)]


if __name__ == "__main__":
    S = Solution()
    print(S.minDistance(word1="horse", word2="rose"))
