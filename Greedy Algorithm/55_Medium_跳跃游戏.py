from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     # 动态规划解法，定义dp[i]为是否能到达i位置
    #     # 超时 74/75
    #     dp = [False] * len(nums)
    #     dp[0] = True
    #     for i in range(len(nums)):
    #         for j in range(min(nums[i], len(nums) - i - 1) + 1):
    #             dp[i + j] = dp[i]
    #
    #     return dp[-1]

    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法
        # 由于数组的值表示能跳到最远的位置，那么一定能到达之前的位置，因此只需要考虑往最远的位置跳
        max_pos = 0
        for i in range(len(nums)):
            if i > max_pos:
                return False
            max_pos = max(max_pos, i + nums[i])

            if max_pos >= len(nums) - 1:
                return True

        return True


if __name__ == "__main__":
    S = Solution()
    print(S.canJump([2, 3, 1, 1, 4]))
    print(S.canJump([3, 2, 1, 0, 4]))
