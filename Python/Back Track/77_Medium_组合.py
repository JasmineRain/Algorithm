from typing import List


class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     ans = []
    #
    #     def backtrack(start, num, trace):
    #         if num == k:
    #             ans.append(trace.copy())
    #             return
    #         for i in range(start, n + 1):
    #             trace.append(i)
    #             num += 1
    #             start = i + 1
    #             backtrack(start, num, trace)
    #             trace.pop()
    #             num -= 1
    #             start -= 1
    #
    #     backtrack(1, 0, [])
    #     return ans
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, num, trace):
            if num == k:
                ans.append(trace)
                return
            for i in range(start, n + 1):
                backtrack(i + 1, num + 1, trace + [i])

        backtrack(1, 0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.combine(n=4, k=2))
