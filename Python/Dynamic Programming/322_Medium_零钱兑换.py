from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for item in coins:
                if i - item >= 0 and dp[i - item] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - item] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - item] + 1)
        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    S = Solution()
    print(S.coinChange(coins=[1, 2, 5], amount=11))
