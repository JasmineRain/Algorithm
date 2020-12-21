from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(start, trace):
            ans.append(trace.copy())
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                start = i + 1
                trace.append(nums[i])
                backtrack(start, trace)
                start -= 1
                trace.pop()

        backtrack(0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.subsetsWithDup(nums=[1, 2, 2]))
