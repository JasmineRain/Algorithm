class Solution:
    def bubbleSort(self, nums):
        for i in range(0, len(nums)):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.bubbleSort(nums)
    print(nums)
