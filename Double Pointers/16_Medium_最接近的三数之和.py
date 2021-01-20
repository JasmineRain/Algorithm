from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if length < 3:
            return 0
        ans = sum(nums[:3])
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                elif total > target:
                    right -= 1
                else:
                    left += 1
                ans = total if abs(total - target) < abs(ans - target) else ans
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
