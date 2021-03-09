from typing import List


class Solution:
    # 回溯法 超时35/45
    # def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    #     flag = [False] * len(group)
    #     ans = 0
    #     MOD = 10**9 + 7
    #     group, profit = zip(*sorted(zip(group, profit), key=lambda x: x[0]))
    #     def backtrack(start, trace, workder, value):
    #         if value >= minProfit:
    #             nonlocal ans
    #             ans += 1
    #             ans %= MOD
    #         for i in range(start, len(group)):
    #             if flag[i]:
    #                 continue
    #             if workder + group[i] > n:
    #                 break
    #             else:
    #                 flag[i] = True
    #                 backtrack(i + 1, trace + [i], workder + group[i], value + profit[i])
    #                 flag[i] = False
    #
    #     backtrack(0, [], 0, 0)
    #     return ans % MOD

    # 动态规划
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 初始化dp表，表第0行初始化为1
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(minProfit)]
        l = len(group)
        # 全任务遍历
        for i in range(l):
            # 针对每项任务，全局更新每种target，cost组合
            # 自底向上，采用原地更新
            for target in reversed(range(minProfit + 1)):
                # 由于cost不能小于0，意味着超员，所以cost>=group[i]
                for cost in reversed(range(group[i], n + 1)):
                    # profit可以小于0，意味着超额收益，将所有超额都归结至profit=0
                    dp[target][cost] += dp[max(0, target - profit[i])][cost - group[i]]
        return int(dp[-1][-1] % 1000000007)


if __name__ == "__main__":
    S = Solution()
    print(S.profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
    print(S.profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))
