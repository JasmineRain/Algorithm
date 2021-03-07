class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 定义dp[i][j]为s1的前i个字符和s2的前j个字符能否组成s3的前(i+j)个字符
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, l2 + 1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(S.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(S.isInterleave(s1="", s2="", s3=""))
