from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k:
            return 0

        count = Counter(s)
        for c in count.keys():
            if count[c] < k:
                return max(self.longestSubstring(item, k) for item in s.split(c))
        return len(s)


if __name__ == "__main__":
    S = Solution()
    print(S.longestSubstring(s="aaabb", k=3))
    print(S.longestSubstring(s="ababbc", k=2))
