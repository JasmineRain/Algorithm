from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        flag = False
        for item in intervals:
            if item[1] < newInterval[0]:
                ans.append(item)
            elif item[0] > newInterval[1]:
                if not flag:
                    ans.append(newInterval)
                    flag = True
                ans.append(item)
            else:
                newInterval = [min(newInterval[0], item[0]), max(newInterval[1], item[1])]
        if not flag:
            ans.append(newInterval)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(S.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
