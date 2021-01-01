import collections
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:

        num = 0
        used = collections.Counter()
        candidate = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)

        for item in candidate:

            if used[item[1]] >= use_limit:
                continue
            else:
                num += item[0]
                used[item[1]] += 1

            if sum(used.values()) == num_wanted:
                return num

        return num


if __name__ == "__main__":
    S = Solution()
    print(S.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], num_wanted=3, use_limit=1))
    print(S.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], num_wanted=3, use_limit=2))
    print(S.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=1))
    print(S.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=2))
