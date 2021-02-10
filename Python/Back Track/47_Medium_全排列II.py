from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        flag = [False] * len(nums)
        nums.sort()
        def backtrack(trace):
            if len(trace) == len(nums):
                ans.append(trace)
                return
            for i in range(0, len(nums)):
                if flag[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not flag[i-1]:
                    continue
                flag[i] = True
                backtrack(trace + [nums[i]])
                flag[i] = False

        backtrack([])
        return ans

    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     flag = [False] * len(nums)
    #     nums.sort()
    #     def backtrack(trace):
    #         if len(trace) == len(nums):
    #             ans.append(trace.copy())
    #             return
    #         for i in range(0, len(nums)):
    #             if flag[i]:
    #                 continue
    #             if i > 0 and nums[i] == nums[i-1] and not flag[i-1]:
    #                 continue
    #             trace.append(nums[i])
    #             flag[i] = True
    #             backtrack(trace)
    #             flag[i] = False
    #             trace.pop()
    #
    #     backtrack([])
    #     return ans


if __name__ == "__main__":
    S = Solution()
    print(S.permuteUnique(nums=[3, 3, 0, 3]))
