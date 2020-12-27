class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        remain = len(num) - k
        for i in range(len(num)):
            while ans and k > 0 and ans[-1] > num[i]:
                ans.pop()
                k -= 1
            ans.append(num[i])

        return "".join(ans[:remain]).lstrip("0") or "0"


if __name__ == "__main__":
    S = Solution()
    print(S.removeKdigits(num="1432219", k=3))
    print(S.removeKdigits(num="10200", k=1))
    print(S.removeKdigits(num="1173", k=2))
