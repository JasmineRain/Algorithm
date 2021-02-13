from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.searchLeft(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.searchRight(nums, target)

        return [left, right]

    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == "__main__":
    S = Solution()
    print(S.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
