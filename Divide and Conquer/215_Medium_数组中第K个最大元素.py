from typing import List
import random


class Solution:

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
    #     nums.sort()
    #     return nums[len(nums) - k]

    def findKthLargest(self, nums: List[int], k: int) -> int:

        left, right = 0, len(nums) - 1
        prev = len(nums) - k

        def partition(start, end):

            # 随机化初始轴，否则耗时会收到极端样例的影响（如倒序样例）
            idx = random.randint(left, right)
            nums[start], nums[idx] = nums[idx], nums[start]
            axis = nums[start]

            while start != end:
                while start < end and nums[end] >= axis:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]
                while start < end and nums[start] <= axis:
                    start += 1
                nums[start], nums[end] = nums[end], nums[start]

            return start

        while True:
            res = partition(left, right)
            if res == prev:
                return nums[res]
            elif res < prev:
                left = res + 1
            else:
                right = res - 1


if __name__ == "__main__":
    S = Solution()
    print(S.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(S.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
