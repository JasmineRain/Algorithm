from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        end = - float("inf")

        for i in range(len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count


if __name__ == "__main__":
    S = Solution()
    print(S.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]))
    print(S.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(S.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(S.eraseOverlapIntervals([[1, 2], [2, 3]]))
