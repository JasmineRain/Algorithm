import collections


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = collections.Counter(s)
        ans = []
        flag = set()
        for c in s:
            if c not in flag:
                while ans and c < ans[-1] and counter[ans[-1]] > 0:
                    flag.discard(ans.pop())
                flag.add(c)
                ans.append(c)
            counter[c] -= 1

        return "".join(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.smallestSubsequence(s="bcabc"))
    print(S.smallestSubsequence(s="cbacdcbc"))
    print(S.smallestSubsequence(s="bbcaac"))
