from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        nums.sort(reverse=True)
        ans = []
        cur = 0
        total = sum(nums)

        for i in range(len(nums)):
            cur += nums[i]
            ans.append(nums[i])

            if cur > total - cur:
                return ans


if __name__ == "__main__":
    S = Solution()
    print(S.minSubsequence(nums=[4, 3, 10, 9, 8]))
    print(S.minSubsequence(nums=[4, 4, 7, 6, 7]))
    print(S.minSubsequence(nums=[6]))
