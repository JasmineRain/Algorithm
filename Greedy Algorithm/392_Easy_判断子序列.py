class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #
    #     if len(s) > len(t):
    #         return False
    #
    #     fast = slow = 0
    #
    #     while slow != len(s):
    #
    #         if fast == len(t):
    #             return False
    #
    #         if s[slow] == t[fast]:
    #             slow += 1
    #             fast += 1
    #         else:
    #             fast += 1
    #
    #     return True

    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n > m:
            return False

        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n


if __name__ == "__main__":
    S = Solution()
    print(S.isSubsequence(s="abc", t="ahbgdc"))
    print(S.isSubsequence(s="axc", t="ahbgdc"))
