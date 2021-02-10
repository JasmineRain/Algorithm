from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        ans = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            ans += right - left + 1

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
