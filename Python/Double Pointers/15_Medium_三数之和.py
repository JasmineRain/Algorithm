from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        if length < 3:
            return []
        res = []
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left -= 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == "__main__":
    S = Solution()
    print(S.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
