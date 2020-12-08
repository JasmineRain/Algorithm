from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dp[i]表示以第i个字符结尾的最大和
        dp = [0] * (len(nums))
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        # print(dp)
        return max(dp)


if __name__ == "__main__":
    S = Solution()
    print(S.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
