from typing import List


class Solution:
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     # 定义dp[k][i][j]为前k个元素内，使用i个0，j个1可以拼成的字符串个数
    #     dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
    #
    #     for k in range(1, len(strs) + 1):
    #         zeros = strs[k - 1].count("0")
    #         ones = strs[k - 1].count("1")
    #         for i in range(m + 1):
    #             for j in range(n + 1):
    #                 dp[k][i][j] = dp[k - 1][i][j]
    #
    #                 if i >= strs[k - 1].count('0') and j >= strs[k - 1].count('1') and dp[k][i][j] < dp[k - 1][i - zeros][j - ones] + 1:
    #                     dp[k][i][j] = dp[k - 1][i - zeros][j - ones] + 1
    #     # print(dp)
    #     return dp[-1][-1][-1]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 这里考虑对状态进行压缩，因为状态的第一维k，状态转移时只与前一项有关
        # 注意遍历顺序，从小至大遍历是不合理的，因为会包含多次选择同一个字符串的情况
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            n0 = s.count('0')
            n1 = s.count('1')
            for i in range(m, n0 - 1, -1):
                for j in range(n, n1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - n0][j - n1] + 1)

        # print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))
