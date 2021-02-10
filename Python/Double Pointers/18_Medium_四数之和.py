from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        length = len(nums)
        if length < 4:
            return []
        res = []
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    total = nums[left] + nums[right] + nums[i] + nums[j]
                    if total == target:
                        res.append([nums[left], nums[right], nums[i], nums[j]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left -= 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == "__main__":
    S = Solution()
    print(S.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
