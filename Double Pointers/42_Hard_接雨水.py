from typing import List


class Solution:
    # 暴力按列求解  超时319/320
    # def trap(self, height: List[int]) -> int:
    #     ans = 0
    #     for i in range(1, len(height) - 1):
    #         left = 0
    #         right = 0
    #         for j in range(0, i):
    #             left = max(left, height[j])
    #         for k in range(i + 1, len(height)):
    #             right = max(right, height[k])
    #         threshold = min(left, right)
    #         # print(i, height[i], threshold)
    #         if threshold <= height[i]:
    #             continue
    #         else:
    #             ans += threshold - height[i]
    #     return ans

    # 使用动态规划优化  先预处理得到左右两侧信息
    # def trap(self, height: List[int]) -> int:
    #
    #     # dp_*[i]表示不包含第i列，左右两侧墙的最低高度
    #     dp_left = [0] * len(height)
    #     dp_right = [0] * len(height)
    #     ans = 0
    #
    #     for i in range(1, len(height)):
    #         dp_left[i] = max(dp_left[i - 1], height[i - 1])
    #     for i in range(len(height) - 2, -1, -1):
    #         dp_right[i] = max(dp_right[i + 1], height[i + 1])
    #
    #     for i in range(1, len(height) - 1):
    #         threshold = min(dp_left[i], dp_right[i])
    #         if threshold <= height[i]:
    #             continue
    #         else:
    #             ans += threshold - height[i]
    #
    #     return ans

    # 双指针
    def trap(self, height: List[int]) -> int:
        ans = 0
        left_max = right_max = 0
        left, right = 1, len(height) - 2

        for i in range(1, len(height) - 1):
            if height[left - 1] < height[right + 1]:
                left_max = max(left_max, height[left - 1])
                if left_max > height[left]:
                    ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right + 1])
                if right_max > height[right]:
                    ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
