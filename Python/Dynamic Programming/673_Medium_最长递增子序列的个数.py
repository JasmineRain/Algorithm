from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 定义dp[i]为以第i个元素结尾的最长递增子序列长度
        dp = [1] * len(nums)

        # 定义count[i]为dp[i]对应的序列数
        count = [1] * len(nums)
        ans = 0

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        # print(dp)
        # print(count)
        for i in range(len(nums)):
            if dp[i] == max(dp):
                ans += count[i]
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
