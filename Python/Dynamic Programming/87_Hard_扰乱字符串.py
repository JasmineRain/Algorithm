class Solution:

    # 动态规划
    # def isScramble(self, s1: str, s2: str) -> bool:
    #     # 定义状态dp[i][i][k] 表示 从s1的第i个字符、s2的第j个字符开始，长度为k的子串是否满足变换关系
    #     # 初始状态 k=1，长度为1的字符串，只有相等才匹配
    #     l1 = len(s1)
    #     l2 = len(s2)
    #     if l1 != l2:
    #         return False
    #     dp = [[[False for _ in range(l1 + 1)] for _ in range(l1)] for _ in range(l1)]
    #     for i in range(l1):
    #         for j in range(l2):
    #             dp[i][j][1] = s1[i] == s2[j]
    #
    #     for l in range(2, l1 + 1):
    #         for i in range(0, l1 - l + 1):
    #             for j in range(0, l1 - l + 1):
    #                 for k in range(1, l):
    #                     if dp[i][j][k] and dp[i+k][j+k][l-k]:
    #                         dp[i][j][l] = True
    #                         break
    #                     if dp[i][j+l-k][k] and dp[i+k][j][l-k]:
    #                         dp[i][j][l] = True
    #                         break
    #     return dp[0][0][-1]

    # 递归
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[-i:], s2[:-i])):
                return True
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.isScramble(s1="great", s2="rgeat"))
    print(S.isScramble(s1="abcde", s2="caebd"))
