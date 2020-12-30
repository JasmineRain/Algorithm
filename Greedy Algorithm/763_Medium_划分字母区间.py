from typing import List
from collections import Counter


class Solution:
    # def partitionLabels(self, S: str) -> List[int]:
    #     count = Counter(S)
    #     exist = Counter()
    #     pre = 0
    #     ans = []
    #
    #     for i in range(len(S)):
    #         if not exist:
    #             exist[S[i]] = count[S[i]] - 1
    #         elif S[i] not in exist and sum(exist.values()) != 0:
    #             exist[S[i]] = count[S[i]] - 1
    #         elif S[i] in exist and sum(exist.values()) != 0:
    #             exist[S[i]] -= 1
    #
    #         if sum(exist.values()) == 0:
    #             ans.append(i + 1 - pre)
    #             pre = i + 1
    #             exist = Counter()
    #     return ans

    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


if __name__ == "__main__":
    S = Solution()
    print(S.partitionLabels(S="ababcbacadefegdehijhklij"))
