from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #
    #     if len(prices) <= 1:
    #         return 0
    #
    #     # 定义dp[i][0][0]为  第i天  完成了0笔交易  不持股   能拥有的最大利润
    #     # 定义dp[i][0][1]为  第i天  完成了0笔交易   持股    能拥有的最大利润
    #     # 定义dp[i][1][0]为  第i天  完成了1笔交易   不持股  能拥有的最大利润
    #     # 定义dp[i][1][1]为  第i天  完成了1笔交易    持股   能拥有的最大利润
    #     dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
    #
    #     dp[0][0][0] = 0
    #     dp[0][0][1] = -prices[0]
    #     dp[0][1][0] = 0
    #     dp[0][1][1] = -prices[0]
    #     dp[0][2][0] = 0
    #     dp[0][2][1] = -prices[0]
    #
    #     for i in range(1, len(prices)):
    #         dp[i][0][0] = dp[i - 1][0][0]
    #
    #         dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
    #         dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
    #
    #         dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
    #         dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])
    #
    #     return max(dp[-1][0][0], dp[-1][0][1], dp[-1][1][0], dp[-1][1][1], dp[-1][2][0])
    def maxProfit(self, prices: List[int]) -> int:

        # 定义dp[i][j][x]为  第i天   完成了j笔交易(买入)   当前持股状态x(0不持股，1持股)   能拥有的最大利润
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        for j in range(3):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]


if __name__ == "__main__":
    S = Solution()
    print(S.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
