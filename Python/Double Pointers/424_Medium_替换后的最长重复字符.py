from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        ans = 0
        exist = Counter()
        while right < len(s):
            exist[s[right]] += 1
            while right - left + 1 - exist.most_common(1)[0][1] > k:
                exist[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.characterReplacement(s="AABABBA", k=1))
    print(S.characterReplacement(s="ABAB", k=2))
