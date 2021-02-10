from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def backtrack(start, value, trace):
            if len(trace) > k:
                return
            if value == n and len(trace) == k:
                ans.append(trace.copy())
                return
            for i in range(start, len(candidates)):
                if value + candidates[i] > n:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                trace.append(candidates[i])
                backtrack(i + 1, value + candidates[i], trace)
                trace.pop()

        backtrack(0, 0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum3(k=3, n=9))
