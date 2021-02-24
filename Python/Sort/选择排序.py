class Solution:
    def selectSort(self, nums):
        for i in range(0, len(nums)):
            target = i
            for j in range(i + 1, len(nums)):
                if nums[target] > nums[j]:
                    target = j
            nums[i], nums[target] = nums[target], nums[i]


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.selectSort(nums)
    print(nums)
