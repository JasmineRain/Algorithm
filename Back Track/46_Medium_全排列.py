from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(trace):
            if len(trace) == len(nums):
                ans.append(trace)
                return
            for num in nums:
                if num in trace:
                    continue
                else:
                    # trace.append(num)
                    backtrack(trace + [num])
                    # trace.pop()

        backtrack([])
        return ans

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #
    #     def backtrack(trace):
    #         if len(trace) == len(nums):
    #             ans.append(trace.copy())
    #             return
    #         for num in nums:
    #             if num in trace:
    #                 continue
    #             else:
    #                 trace.append(num)
    #                 backtrack(trace)
    #                 trace.pop()
    #
    #     backtrack([])
    #     return ans


if __name__ == "__main__":
    S = Solution()
    print(S.permute(nums=[1, 2, 3]))
