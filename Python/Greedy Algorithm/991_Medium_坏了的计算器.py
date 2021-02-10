class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:

        # 正向操作需要考虑两条路径  一条为超过Y然后缩减到Y  另一条为先缩减然后正好到Y
        # 情况复杂，考虑反向操作
        step = 0
        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y //= 2
            step += 1

        return step + X - Y


if __name__ == "__main__":
    S = Solution()
    print(S.brokenCalc(X=2, Y=3))
    print(S.brokenCalc(X=3, Y=10))
    print(S.brokenCalc(X=1024, Y=1))
    print(S.brokenCalc(X=1, Y=1000000000))
