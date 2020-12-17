class Solution:
    def minCut(self, s: str) -> int:
        # dp1[i][j]代表第i个字符到第j个字符构成的子串是否为回文串
        # 预处理字符串
        dp1 = [[False for _ in range(len(s))] for _ in range(len(s))]
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if i == j:
                    dp1[i][j] = True
                elif j - i == 1:
                    dp1[i][j] = s[i] == s[j]
                else:
                    dp1[i][j] = s[i] == s[j] and dp1[i + 1][j - 1]
        # 定义dp2[i]代表前i个字符组成的串至少需要多少次切割才能满足要求
        dp2 = [i for i in range(len(s))]
        for i in range(1, len(s)):
            if dp1[0][i]:
                dp2[i] = 0
            else:
                dp2[i] = min([dp2[j] + 1 for j in range(i) if dp1[j + 1][i]])
        return dp2[-1]


if __name__ == "__main__":
    S = Solution()
    print(S.minCut(s="aab"))
