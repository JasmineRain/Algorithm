from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #
    #     def backtrack(start, trace):
    #         ans.append(trace)
    #         if start == len(nums):
    #             return
    #         for i in range(start, len(nums)):
    #             backtrack(i + 1, trace + [nums[i]])
    #
    #     backtrack(0, [])
    #     return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, trace):
            ans.append(trace.copy())
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                start = i + 1
                trace.append(nums[i])
                backtrack(start, trace)
                start -= 1
                trace.pop()

        backtrack(0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.subsets(nums=[1, 2, 3]))
