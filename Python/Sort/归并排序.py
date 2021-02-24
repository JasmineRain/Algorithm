class Solution:
    def mergeSort(self, nums, start, end):
        self.sort(nums, start, end)

    def sort(self, nums, start, end):
        if start == end:
            return
        mid = (start + end) // 2
        self.sort(nums, start, mid)
        self.sort(nums, mid + 1, end)
        self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        temp = [0] * (end - start + 1)
        left, right = start, mid + 1
        index = 0
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1
        nums[start: end + 1] = temp


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.mergeSort(nums, 0, len(nums) - 1)
    print(nums)
