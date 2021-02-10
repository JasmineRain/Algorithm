from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0

        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1

        return patches


if __name__ == "__main__":
    S = Solution()
    print(S.minPatches(nums=[1, 3], n=6))
    print(S.minPatches(nums=[1, 5, 10], n=20))
    print(S.minPatches(nums=[1, 2, 2], n=5))
