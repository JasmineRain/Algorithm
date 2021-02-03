from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = right = 0
        cur = Counter()
        count = 0
        ans = [0, float("inf")]

        while right < len(s):
            char = s[right]
            if char in need:
                cur[char] += 1
                if cur[char] == need[char]:
                    count += 1
            right += 1
            while count == len(need):
                if right - left < ans[1] - ans[0]:
                    ans = [left, right]
                remove = s[left]
                if remove in need:
                    cur[remove] -= 1
                    if cur[remove] < need[remove]:
                        count -= 1
                left += 1
        return s[ans[0]: ans[1]] if left > 0 else ""


if __name__ == "__main__":
    S = Solution()
    print(S.minWindow(s="ab", t="a"))
