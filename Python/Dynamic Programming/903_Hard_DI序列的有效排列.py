class Solution:

    # 回溯法 超时 68/83
    # def numPermsDISequence(self, S: str) -> int:
    #
    #     res = []
    #     flag = [False] * (len(S) + 1)
    #
    #     def backtrack(trace):
    #         if len(trace) == len(S) + 1:
    #             res.append(trace)
    #
    #         for i in range(len(S) + 1):
    #             if not flag[i] and ((S[len(trace) - 1] == "D" and i < trace[-1]) or (S[len(trace) - 1] == "I" and i > trace[-1])):
    #                 flag[i] = True
    #                 backtrack(trace + [i])
    #                 flag[i] = False
    #
    #     for i in range(len(S) + 1):
    #         flag[i] = True
    #         backtrack([i])
    #         flag[i] = False
    #     return len(res) % (10**9 + 7)

    # 动态规划
    def numPermsDISequence(self, S: str) -> int:

        MOD = (10 ** 9 + 7)

        # 定义dp为满足要求的，由前i + 1个数[0, i]组成的，且最后一个数字为j的序列总数
        dp = [[0 for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]
        dp[0][0] = 1

        for i in range(1, len(S) + 1):
            for j in range(len(S) + 1):
                if S[i - 1] == "D":
                    dp[i][j] += sum(dp[i - 1][k] % MOD for k in range(j, i)) % MOD
                else:
                    dp[i][j] += sum(dp[i - 1][k] % MOD for k in range(j)) % MOD

        return sum(dp[-1]) % MOD


if __name__ == "__main__":
    S = Solution()
    print(S.numPermsDISequence("DID"))
