from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices:
            return 0

        # 定义dp[i][j][x]为  第i天   完成了j笔交易(买入)   当前持股状态x(0不持股，1持股)   能拥有的最大利润
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices))]
        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]


if __name__ == "__main__":
    S = Solution()
    print(S.maxProfit(k = 2, prices = [3,2,6,5,0,3]))
