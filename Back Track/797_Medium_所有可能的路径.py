from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        reachable = [[False for _ in range(len(graph))] for _ in range(len(graph))]
        n = len(graph)
        for i in range(n):
            for j in graph[i]:
                reachable[i][j] = True

        ans = []

        def backtrack(cur, trace):
            if cur == n - 1:
                ans.append([0] + trace)

            if len(trace) == n:
                return

            for i in range(n):
                if reachable[cur][i]:
                    backtrack(i, trace + [i])
        if any(reachable[i][-1] for i in range(n)):
            backtrack(0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
