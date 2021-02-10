from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        left = right = 0
        cur = Counter()
        l1 = len(s1)
        l2 = len(s2)
        while right < l2:
            char = s2[right]
            cur[char] += 1
            while cur[char] > need[char]:
                cur[s2[left]] -= 1
                left += 1
            if right - left + 1 == l1:
                return True
            right += 1

        return False


if __name__ == "__main__":
    S = Solution()
    print(S.checkInclusion(s1="ab", s2="eidbaooo"))
    print(S.checkInclusion(s1="ab", s2="eidboaoo"))
