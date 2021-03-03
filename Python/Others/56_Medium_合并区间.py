from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(S.merge(intervals=[[1, 4], [4, 5]]))
