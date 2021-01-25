from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = p1 = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 != p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
        # print(nums)


if __name__ == "__main__":
    S = Solution()
    print(S.sortColors(nums=[2, 0, 2, 1, 1, 0]))
