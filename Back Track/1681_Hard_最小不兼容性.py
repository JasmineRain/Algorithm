import collections
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        l = len(nums)
        n = l // k
        if n == 0 or n == 1:
            return 0
        counter = collections.Counter(nums)
        if max(counter.values()) > k:
            return -1
        keys = sorted(counter.keys())
        ans = float('inf')

        def backtrack(idx, cur_num, cur_list, delta):
            nonlocal ans
            if delta >= ans: return
            if len(cur_list) == n:
                delta += cur_list[-1] - cur_list[0]
                cur_list = []
                cur_num = -1
            if idx == l:
                ans = min(ans, delta)
                return
            for i in keys:
                if i <= cur_num or counter[i] == 0:
                    continue
                counter[i] -= 1
                cur_list.append(i)
                backtrack(idx + 1, i, cur_list, delta)
                cur_list.pop()
                counter[i] += 1
                if len(cur_list) == 0:
                    break

        backtrack(0, -1, [], 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.minimumIncompatibility(nums=[6, 3, 8, 1, 3, 1, 2, 2], k=4))
