from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        if len(nums) <= 1:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i + 1 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        s = i + 1
        e = len(nums) - 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1


if __name__ == "__main__":
    S = Solution()
    nums = []
    S.nextPermutation(nums=nums)
    print(nums)
