from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start, value, trace):
            if value == target:
                ans.append(trace.copy())
                return
            for i in range(start, len(candidates)):
                if value + candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                trace.append(candidates[i])
                backtrack(i + 1, value + candidates[i], trace)
                trace.pop()

        backtrack(0, 0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
