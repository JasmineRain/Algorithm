from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 定义dp[i]为 *以第i个元素结尾的* 摆动序列的长度----不可行
        # 定义两个数组，up[i]表示  以第i个元素结尾，且第i个元素相比前一个元素是上升的  这样的摆动序列长度
        #            down[i]表示  以第i个元素结尾，且第i个元素相比前一个元素是下降的  这样的摆动序列长度

        if len(nums) < 2:
            return len(nums)

        up = [1] * len(nums)
        down = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        # print(up)
        # print(down)
        return max(up[-1], down[-1])


if __name__ == "__main__":
    S = Solution()
    print(S.wiggleMaxLength(nums=[3, 3, 3, 2, 5]))
