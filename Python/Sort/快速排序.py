class Solution:
    def quickSort(self, nums, start, end):
        if start < end:
            index = self.partition(nums, start, end)
            self.quickSort(nums, 0, index - 1)
            self.quickSort(nums, index + 1, end)

    def partition(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.quickSort(nums, 0, len(nums) - 1)
    print(nums)
