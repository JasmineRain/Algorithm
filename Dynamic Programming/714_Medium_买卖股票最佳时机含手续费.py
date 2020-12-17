from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if len(prices) <= 1:
            return 0

        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # 定义dp[i][0]为第i天不持股，能拥有的最大利润
        # 定义dp[i][1]为第i天持股，能拥有的最大利润
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        # print(dp)
        return dp[len(prices) - 1][0]


if __name__ == "__main__":
    S = Solution()
    print(S.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
