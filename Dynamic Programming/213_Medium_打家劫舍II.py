from typing import List


class Solution:
    def _rob(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0

        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])

    def rob(self, nums: List[int]) -> int:

        s1 = self._rob(nums=nums[2:len(nums) - 1])
        s2 = self._rob(nums=nums[1:])
        return max(s1 + nums[0], s2)


if __name__ == "__main__":
    S = Solution()
    print(S.rob(nums=[1, 2, 3, 1]))
