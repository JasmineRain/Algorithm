class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        carry = 0
        la = len(a)
        lb = len(b)
        ans = []
        for i in range(0, length):
            carry += int(a[la - 1 - i]) if i < la else 0
            carry += int(b[lb - 1 - i]) if i < lb else 0
            ans.append(str(carry % 2))
            carry //= 2
        if carry:
            ans.append("1")
        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.addBinary(a="11", b="1"))
    print(S.addBinary(a="1010", b="1011"))
