from typing import List
from collections import Counter
import heapq


class Solution:
    # 排序后滑窗
    # def smallestRange(self, nums: List[List[int]]) -> List[int]:
    #     merged = []
    #     ans = [-float("inf"), float("inf")]
    #     for i in range(len(nums)):
    #         for j in range(len(nums[i])):
    #             merged.append([nums[i][j], i])
    #     merged.sort(key=lambda x: x[0])
    #     left = right = 0
    #     exist = Counter()
    #     while right < len(merged):
    #         exist[merged[right][1]] += 1
    #         while len(exist) == len(nums):
    #             if merged[right][0] - merged[left][0] < ans[1] - ans[0]:
    #                 ans[1], ans[0] = merged[right][0], merged[left][0]
    #             exist[merged[left][1]] -= 1
    #             if exist[merged[left][1]] <= 0:
    #                 exist.pop(merged[left][1])
    #             left += 1
    #         right += 1
    #     return ans


    # 利用队列维护区间
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        ans = [-float("inf"), float("inf")]
        max_value = -float("inf")
        for i in range(len(nums)):
            heapq.heappush(heap, [nums[i][0], i, 0])
            max_value = max(max_value, nums[i][0])
        while len(heap) == len(nums):
            item = heapq.heappop(heap)
            if max_value - item[0] < ans[1] - ans[0]:
                ans = [item[0], max_value]
            if item[2] + 1 < len(nums[item[1]]):
                heapq.heappush(heap, [nums[item[1]][item[2]+1], item[1], item[2] + 1])
                max_value = max(max_value, nums[item[1]][item[2]+1])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.smallestRange(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
