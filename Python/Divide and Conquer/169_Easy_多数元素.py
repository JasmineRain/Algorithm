import collections


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    S = Solution()
    print(S.majorityElement([2, 2, 1, 1, 1, 2, 2]))
