class Solution:
    def insertSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    continue
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.insertSort(nums)
    print(nums)
