from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        product = 1
        ans = 0
        while right < len(nums):
            product *= nums[right]
            right += 1
            while product >= k:
                product /= nums[left]
                left += 1


if __name__ == "__main__":
    S = Solution()
    print(S.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
