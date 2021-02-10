from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = cost[0]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i-1]
        # print(dp)
        return min(dp[-1], dp[-2])


if __name__ == "__main__":
    S = Solution()
    print(S.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
