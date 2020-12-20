from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start, value, trace):
            if value == target:
                ans.append(trace.copy())
                return
            for i in range(start, len(candidates)):
                value += candidates[i]
                if value > target:
                    break
                trace.append(candidates[i])
                backtrack(i, value, trace)
                value -= candidates[i]
                trace.pop()

        backtrack(0, 0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum(candidates=[2, 3, 5], target=8))
