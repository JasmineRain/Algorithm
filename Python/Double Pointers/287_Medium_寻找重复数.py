from typing import List


class Solution:
    # 二分查找
    # def findDuplicate(self, nums: List[int]) -> int:
    #     left, right = 1, len(nums) - 1
    #     while left < right:
    #         target = (left + right) // 2
    #         total = 0
    #         for num in nums:
    #             if num <= target:
    #                 total += 1
    #         if total > target:
    #             right = target
    #         else:
    #             left = target + 1
    #     return left

    # 构建环
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = ans = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while ans != slow:
            ans = nums[ans]
            slow = nums[slow]

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.findDuplicate(nums=[1, 3, 4, 2, 2]))
