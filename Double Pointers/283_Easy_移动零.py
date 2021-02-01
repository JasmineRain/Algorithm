from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0

        while fast <= len(nums) - 1:
            if nums[fast]


if __name__ == "__main__":
    S = Solution()
    print(S.moveZeroes([0, 1, 0, 3, 12]))
