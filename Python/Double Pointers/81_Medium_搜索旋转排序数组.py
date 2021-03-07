from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                left += 1
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
    print(S.search(nums=[1, 0, 1, 1, 1], target=0))
    print(S.search(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2))
