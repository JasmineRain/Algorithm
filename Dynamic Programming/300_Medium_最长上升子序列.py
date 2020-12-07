from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义dp[i]为*以第i个字符结尾的*子数组的最长上升子序列的长度

        if not nums:
            return 0

        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)


if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLIS(nums=[1,3,6,7,9,4,10,5,6]))
