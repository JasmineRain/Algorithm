from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        
        # 找准状态，状态一共只有3种情况：持股、不持股不冷冻、不持股冷冻
        # 定义dp[i][0]代表持股    dp[i][1]代表不持股不冷冻    dp[i][2]代表不持股冷冻    ~情况下的收益
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i]

            # print(dp)
        return max(dp[-1][1], dp[-1][2])


if __name__ == "__main__":
    S = Solution()
    print(S.maxProfit(prices=[7, 1, 5, 3, 6, 7, 4]))
