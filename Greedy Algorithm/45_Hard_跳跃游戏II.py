from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     # 动态规划解法，定义dp[i]为到达i位置需要的最小跳动次数
    #     # 超时62/95
    #     dp = [float("inf")] * len(nums)
    #     dp[0] = 0
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[j] + j >= i:
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #
    #     return dp[-1]

    # def jump(self, nums: List[int]) -> int:
    #     # 贪心算法  当前位于位置i时，假设可跳到 i + 1 至 j 几个位置上   那么选择其中下一步可以到达最远点的那个位置k
    #     # 合理性在于：假设k为i + 1 至 j 中，能到达最远点的位置，如果有另一个位置，其达到的位置不如k远，但是下一步能达到比k下一步更远的位置
    #     # 那么可以从k先跳到这个位置  再进行后续跳跃   次数并没有因为选择k而多出一步
    #     max_pos = 0
    #     start = 0
    #     step = 0
    #     end = 1
    #     while end < len(nums):
    #         for i in range(start, end):
    #             max_pos = max(max_pos, i + nums[i])
    #
    #         start = end
    #         end = max_pos + 1
    #         step += 1
    #     return step

    def jump(self, nums: List[int]) -> int:
        # 贪心算法优化
        max_pos = 0
        step = 0
        end = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)

            if i == end:
                step += 1
                end = max_pos
        return step


if __name__ == "__main__":
    S = Solution()
    print(S.jump([2, 3, 1, 1, 4]))
    print(S.jump([1, 2]))
