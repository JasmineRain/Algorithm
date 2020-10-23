from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left != right:
            current_volume = min(height[left], height[right]) * (right - left)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            if current_volume > max_volume:
                max_volume = current_volume
        return max_volume


if __name__ == "__main__":
    S = Solution()
    print(S.maxArea([1,8,6,2,5,4,8,3,7]))



