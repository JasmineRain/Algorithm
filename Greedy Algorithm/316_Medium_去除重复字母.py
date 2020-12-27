import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
    print(S.removeDuplicateLetters(s="bcabc"))
    print(S.removeDuplicateLetters(s="cbacdcbc"))
    print(S.removeDuplicateLetters(s="bbcaac"))
