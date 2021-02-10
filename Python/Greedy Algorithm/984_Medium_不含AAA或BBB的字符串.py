class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = [""] * (a + b)
        index = 0
        round = 1
        ca = a
        cb = b

        if a >= b:
            while ca > 0:
                ans[index] = "a"
                ca -= 1
                index += 3
                if index >= (a + b):
                    index = round
                    round += 1

            while cb > 0:
                ans[index] = "b"
                cb -= 1
                index += 3
                if index >= (a + b):
                    index = round
                    round += 1

            return "".join(ans)
        else:
            while cb > 0:
                ans[index] = "b"
                cb -= 1
                index += 3
                if index >= (a + b):
                    index = round
                    round += 1
            while ca > 0:
                ans[index] = "a"
                ca -= 1
                index += 3
                if index >= (a + b):
                    index = round
                    round += 1

            return "".join(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.strWithout3a3b(a=1, b=2))
    print(S.strWithout3a3b(a=4, b=1))
    print(S.strWithout3a3b(a=1, b=3))
