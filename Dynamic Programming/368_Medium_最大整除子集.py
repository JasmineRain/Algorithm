from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        nums.sort()
        # dp[i]表示以num[i]结尾的最大整除子集
        dp = [[] for _ in range(len(nums))]
        dp[0].append(nums[0])
        for i in range(1, len(nums)):
            dp[i].append(nums[i])
            max_length = 0
            max_idx = 0
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) >= max_length:
                        max_length = len(dp[j])
                        max_idx = j
            if max_length >= 1:
                dp[i] = [item for item in dp[max_idx]]
                dp[i].append(nums[i])

        idx = 0
        length = 0
        for i in range(len(nums)):
            if len(dp[i]) > length:
                idx = i
                length = len(dp[i])
        # print(dp)
        return dp[idx]


if __name__ == "__main__":
    S = Solution()
    print(S.largestDivisibleSubset(nums=[343, 49, 8, 4, 2, 1]))
