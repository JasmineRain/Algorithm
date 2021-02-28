from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            dist = [0] * 26
            for c in s:
                dist[ord(c) - ord('a')] += 1
            ans[tuple(dist)].append(s)
        return list(ans.values())


if __name__ == "__main__":
    S = Solution()
    print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
